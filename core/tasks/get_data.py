import psycopg2
import pandas as pd
from typing import Optional, Dict, TypeVar

from datetime import datetime
from celery import shared_task
from django.db import transaction

from core.tasks import queries
from utils.decorators import log_time
from utils.db import connect_db, cursor_fetch_iterator, CursorWrapper
from utils.transformations import batched
from core.models import (
    ToFetchProject,
    Project,
    Lead,
    Entry,
    AFMapping,
    Organization,
    DeepDataFetchTracker,
)
from .get_data_old import get_tags_data_for_exportable
from .nlp_mapping import (
    get_geolocation_dict,
    get_mapping_sheet,
    get_nlp_outputs
)
from core_server.settings import FETCH_DEEP_PROJECTS_AFTER

from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

T = TypeVar("T")
OptDictIntObj = Optional[Dict[int, T]]

# Data will be fetched later than the following date
VERY_PAST_DATE = datetime(1990, 10, 10)  # Before creation of deep platform


def get_projects_later_than_date():
    try:
        return datetime.strptime("%Y-%m-%d", FETCH_DEEP_PROJECTS_AFTER)
    except ValueError:
        # We want projects only after 2021. Projects created before 2021 are not that relevant
        return datetime(2021, 1, 1)


@shared_task(name="core.tasks.get_data.fetch_new_projects")
def fetch_new_projects():
    """
    This fetches projects not added to db and which have at least 10 leads in
    them and also updates the active_status of project if already exists.
    """
    cursor = connect_db()
    try:
        projects_later_than_date = get_projects_later_than_date()
        cursor.execute(queries.new_projects_q.format(projects_later_than_date))
        projects_raw = cursor.fetchall()
    except psycopg2.ProgrammingError as e:
        logger.warning(f"Failed to fetch projects. {e}")
        return
    with transaction.atomic():
        columns = [c.name for c in cursor.description]
        projects_rows = [dict(zip(columns, row)) for row in projects_raw]
        for row in projects_rows:
            ToFetchProject.objects.update_or_create(
                original_project_id=row["id"],
                defaults={
                    "active_status": row["status"],
                }
            )


@shared_task(name="core.tasks.get_data.fetch_deep_data")
@log_time(log_function=logger.info)
def fetch_deep_data():
    tracker = DeepDataFetchTracker.objects.first()
    if tracker is None:
        tracker = DeepDataFetchTracker.objects.create()
    cursor = connect_db()
    try:
        afs_dict = fetch_afs(cursor, tracker)
        orgs_dict = fetch_orgs(cursor, tracker)
        if orgs_dict is None:
            logger.warning(
                "Could not fetch orgs. Continuing without orgs, some lead fields may be null"
            )  # noqa
        if afs_dict is None:
            logger.warning("Could not fetch analysis frameowrks. Exiting.")
            return
        for prj in (
            ToFetchProject.objects.filter(
                status__in=[ToFetchProject.FetchStatus.NOT_FETCHED, ToFetchProject.FetchStatus.FETCHING]
            )
        ):
            fetch_project_data(cursor, prj, afs_dict, orgs_dict or {})
            logger.info(
                f"Fetched deep project with id {prj.original_project_id}"
            )  # noqa
    finally:
        cursor.cursor.close()
        cursor.connection.close()


def fetch_project_data(
    cursor: CursorWrapper,
    to_fetch: ToFetchProject,
    afs_dict: Dict[int, int],
    orgs_dict: Dict[int, int],
):
    # Set status to fetching
    to_fetch.status = ToFetchProject.FetchStatus.FETCHING
    to_fetch.save(update_fields=["status"])
    pid = to_fetch.original_project_id
    logger.info(f"Fetching data for deep project {pid}")
    try:
        cursor.execute(queries.projects_q.format(pid))
        data = cursor.fetchall()
        if not data:
            logger.warning("no project", pid)
            to_fetch.status = ToFetchProject.FetchStatus.NOT_FOUND
            to_fetch.save(update_fields=["status"])
            return
    except psycopg2.ProgrammingError:
        to_fetch.status = ToFetchProject.FetchStatus.ERRORED
        to_fetch.save(update_fields=["status"])
    else:
        columns = [c.name for c in cursor.description]
        project_dict = dict(zip(columns, data[0]))
        afid = project_dict["analysis_framework_id"]
        if afid is not None and afid not in afs_dict:
            to_fetch.status = ToFetchProject.FetchStatus.NOT_FOUND
            to_fetch.error = "Af not found for project"
            to_fetch.save(update_fields=["status", "error"])
            logger.warning(
                f"Could not find DEEP af with id {afid} and project id {pid}. Skipping."
            )  # noqa
            return
        if len(data) == 0:
            logger.warning(
                f"Could not find DEEP project with id {pid}. Skipping."
            )  # noqa
            to_fetch.status = ToFetchProject.FetchStatus.NOT_FOUND
            to_fetch.save(update_fields=["status"])
            return
        project, _ = Project.objects.update_or_create(
            original_project_id=to_fetch.original_project_id,
            defaults={
                "af_mapping_id": afs_dict.get(afid),
                "to_fetch_project": to_fetch,
                "title": project_dict["title"],
                "location": "",  # TODO: To discuss what to put in here
                "description": project_dict["description"],
                "extra": {k: str(project_dict[k]) for k in ["start_date", "end_date"]},
            },
        )
        logger.info(f"Fetched project data for deep project {pid}")

        leads_dict = fetch_project_leads(cursor, project, orgs_dict)
        if not project.af_mapping:
            logger.warning(f"Project with id:{project.original_project_id} does not have analysis framework")
            return
        if leads_dict:
            fetch_project_entries(cursor, project, leads_dict)

        logger.info(f"Fetched all data for deep project {pid}")


def _process_lead_batch(lead_batch, project, orgs_dict, columns) -> dict:
    lead_extra_fields = [
        "author_raw",
        "source_raw",
        "priority",
        "status",
        "published_on",
    ]
    last_lead_dict = {}
    for lead in lead_batch:
        last_lead_dict = dict(zip(columns, lead))
        auth_id = last_lead_dict["author_id"]
        source_id = last_lead_dict["source_id"]
        Lead.objects.update_or_create(
            original_lead_id=last_lead_dict["id"],
            defaults={
                "project": project,
                "authoring_org_id": orgs_dict.get(auth_id),
                "publishing_org_id": orgs_dict.get(source_id),
                "extraction_status": last_lead_dict["extraction_status"],
                "title": last_lead_dict["title"],
                "text_extract": last_lead_dict["text_extract"],
                "source_url": last_lead_dict["url"],
                "confidentiality": last_lead_dict["confidentiality"],
                "extra": {k: str(last_lead_dict[k]) for k in lead_extra_fields},
            },
        )
    return last_lead_dict


def fetch_project_leads(
    cursor: CursorWrapper,
    project: Project,
    orgs_dict: Dict[int, int],
) -> OptDictIntObj[int]:
    pid = project.original_project_id
    try:
        last_fetched = project.to_fetch_project.last_fetched_lead_created_at
        cursor.execute(
            queries.lead_q.format(pid, last_fetched or VERY_PAST_DATE)
        )  # noqa
        rows = cursor_fetch_iterator(cursor, 3000)
    except psycopg2.ProgrammingError as e:
        logger.warning(f"Error fetching leads for deep project {pid}: {e}")
        return
    else:
        columns = []
        # fetched in asc order
        batch_size = 1
        for i, row_batch in enumerate(batched(rows, batch_size)):
            columns = (
                columns if columns else [c.name for c in cursor.description]
            )  # noqa
            with transaction.atomic():
                last_lead_dict = _process_lead_batch(
                    row_batch, project, orgs_dict, columns
                )  # noqa
                project.to_fetch_project.last_fetched_lead_created_at = last_lead_dict[
                    "created_at"
                ]  # noqa
                project.to_fetch_project.save()
    return dict(Lead.objects.values_list("original_lead_id", "id"))


def _process_entries_batch(
    entries_batch,
    leads_dict,
    columns,
    widget_id_labels: dict,
    geo_locations_dict: dict,
    mapping_sheet: pd.DataFrame,
) -> dict:
    entry_extra_fields = [
        "entry_type",
        "excerpt_modified",
    ]
    current_entry_dict = {}
    for row in entries_batch:
        current_entry_dict = dict(zip(columns, row))
        lead_id = leads_dict.get(current_entry_dict["lead_id"])
        if lead_id is None:
            logger.warning("no lead for lead id", current_entry_dict["lead_id"])
            continue
        exp_data = current_entry_dict["export_data"]
        manual_tagged_data = format_manual_tags(exp_data, widget_id_labels)
        nlp_tags, nlp_mapping = get_nlp_outputs(manual_tagged_data, mapping_sheet, geo_locations_dict)

        Entry.objects.update_or_create(
            original_entry_id=current_entry_dict["id"],
            lead_id=lead_id,
            defaults={
                "original_lang": "",
                "excerpt": current_entry_dict["excerpt"],
                "original_af_tags": manual_tagged_data,
                "nlp_tags": nlp_tags,
                "nlp_mapping": nlp_mapping,
                "export_data": exp_data,
                "extra": {k: current_entry_dict[k] for k in entry_extra_fields},
                "deep_entry_created_at": current_entry_dict["created_at"],
            },
        )
    return current_entry_dict


def fetch_project_entries(
    cursor: CursorWrapper,
    project: Project,
    leads_dict: Dict[int, int],
):
    af_mapping = project.af_mapping
    # These are to convert subsectors/subpillars key to corresponding label
    # which is required by the nlp services
    widget_id_labels = get_widget_id_to_label_dict(af_mapping)
    geo_locations_dict = get_geolocation_dict(cursor=cursor)

    mapping_sheet = get_mapping_sheet()

    pid = project.original_project_id
    try:
        last_fetched = project.to_fetch_project.last_fetched_entry_created_at
        cursor.execute(
            queries.entries_exportable_grouped_q.format(pid, last_fetched or VERY_PAST_DATE)
        )
        rows = cursor_fetch_iterator(cursor, 3000)
    except psycopg2.ProgrammingError as e:
        logger.warning(f"Error fetching entries for deep project {pid}: {e}")
        return
    else:
        columns = []
        batch_size = 20
        for i, row_batch in enumerate(batched(rows, batch_size)):
            # NOTE: Although it seems like we can move columns before the loop,
            # but since it is just an iterator, there is nothing available
            # inside the cursor until inside this loop.
            columns = columns if columns else [c.name for c in cursor.description]
            with transaction.atomic():
                last_entry_dict = _process_entries_batch(
                    row_batch,
                    leads_dict,
                    columns,
                    widget_id_labels,
                    geo_locations_dict,
                    mapping_sheet
                )
                to_fetch = project.to_fetch_project
                to_fetch.last_fetched_entry_created_at = last_entry_dict["created_at"]
                to_fetch.save()
    logger.info(f"fetched entries for project {pid}")


def fetch_afs(
    cursor: CursorWrapper, tracker: DeepDataFetchTracker
) -> OptDictIntObj[int]:
    af_extra_fields = ["description", "properties"]
    try:
        last_fetched = tracker.last_fetched_af_created_at
        # fetched with created at ascending order
        cursor.execute(queries.af_q.format(last_fetched or VERY_PAST_DATE))
        rows = cursor_fetch_iterator(cursor)
    except psycopg2.ProgrammingError as e:
        logger.warning("Error fetching afs: " + repr(e))
        return
    else:
        columns = []
        for row in rows:
            columns = (
                columns if columns else [c.name for c in cursor.description]
            )  # noqa
            af_dict = dict(zip(columns, row))
            widgets_data = {
                "widget_keys": af_dict["widget_keys"],
                "widget_ids": af_dict["widget_ids"],
                "widget_titles": af_dict["widget_titles"],
                "widget_properties": af_dict["widget_properties"],
                "widget_versions": af_dict["widget_versions"],
            }
            extra_data = {
                "widgets_data": widgets_data,
                **{k: af_dict[k] for k in af_extra_fields},
            }
            with transaction.atomic():
                AFMapping.objects.update_or_create(
                    original_af_id=af_dict["id"],
                    defaults={
                        "af_name": af_dict["title"],
                        "original_af_tags": {},  # TODO: Fill this up
                        "nlp_tags": {},  # TODO: Fill this up
                        "is_mapped_manually": False,  # TODO: find the value
                        "extra": extra_data,
                    },
                )
                tracker.last_fetched_af_created_at = af_dict["created_at"]
                tracker.save()
        logger.info("fetched afs")
        return dict(AFMapping.objects.values_list("original_af_id", "id"))


def fetch_orgs(
    cursor: CursorWrapper, tracker: DeepDataFetchTracker
) -> OptDictIntObj[int]:
    org_extra_fields = ["url", "source", "parent_id", "organization_type"]
    try:
        last_fetched = tracker.last_fetched_org_created_at
        # fetched with created at ascending order
        cursor.execute(queries.org_q.format(last_fetched or VERY_PAST_DATE))
        rows = cursor_fetch_iterator(cursor)
    except psycopg2.ProgrammingError as e:
        logger.warning("Error fetching afs: " + repr(e))
        return
    else:
        columns = []
        for row in rows:
            columns = (
                columns if columns else [c.name for c in cursor.description]
            )  # noqa
            org_dict = dict(zip(columns, row))
            with transaction.atomic():
                Organization.objects.update_or_create(
                    original_organization_id=org_dict["id"],
                    defaults={
                        "name": org_dict["title"],
                        "short_name": org_dict["short_name"],
                        "long_name": org_dict["long_name"],
                        "extra": {k: org_dict[k] for k in org_extra_fields},
                    },
                )
                tracker.last_fetched_org_created_at = org_dict["created_at"]
                tracker.save()
        return dict(Organization.objects.values_list("original_organization_id", "id"))


def get_widget_id_to_label_dict(af: AFMapping) -> dict:
    widgets_data = af.extra.get("widgets_data")
    if widgets_data is None:
        return {}
    ids = widgets_data["widget_ids"]
    props = widgets_data["widget_properties"]

    mapping = {}
    for wid, prop in zip(ids, props):
        if wid != "matrix2dWidget":
            continue
        for p in prop.get("rows", []):
            mapping[p["key"]] = p["label"]
            for pp in p.get("subRows", []):
                mapping[pp["key"]] = pp["label"]
            for pp in p.get("cells", []):
                mapping[pp["key"]] = pp["label"]

        for p in prop.get("columns", []):
            mapping[p["key"]] = p["label"]
            for pp in p.get("subColumns", []):
                mapping[pp["key"]] = pp["label"]
    return mapping


def format_manual_tags(total_tags: dict, id2label: dict) -> dict:
    results = {}
    for tag in total_tags:
        d = get_tags_data_for_exportable(tag, id2label)
        # not sure if it's possibile (at deep side) that an entry has more
        # elements of the same widget. it will be more safe to check if "d" key
        # is already present in "results" and exteding the corresponding value.
        results.update(d)
    return results
