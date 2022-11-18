import psycopg2
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

from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

T = TypeVar('T')
OptDictIntObj = Optional[Dict[int, T]]

# Data will be fetched later than the following date
VERY_PAST_DATE = datetime(1990, 10, 10)   # Before creation of deep platform


@log_time()
def fetch_deep_data():
    tracker = DeepDataFetchTracker.objects.first()
    if tracker is None:
        tracker = DeepDataFetchTracker.objects.create()
    print('connecting')
    cursor = connect_db()
    print('connected')
    try:
        afs_dict = fetch_afs(cursor, tracker)
        orgs_dict = fetch_orgs(cursor, tracker)
        if orgs_dict is None:
            logger.warning('Could not fetch orgs. Continuing without orgs, some lead fields may be null')  # noqa
        if afs_dict is None:
            logger.warning('Could not fetch analysis frameowrks. Exiting.')
            return
        not_fetched = ToFetchProject.FetchStatus.NOT_FETCHED
        for prj in ToFetchProject.objects.filter(status=not_fetched):
            print(f'Fetching deep project with id {prj.original_project_id}')  # noqa
            logger.info(f'Fetching deep project with id {prj.original_project_id}')  # noqa
            fetch_project_data(
                cursor,
                prj,
                afs_dict,
                orgs_dict or {}
            )
            logger.info(f'Fetched deep project with id {prj.original_project_id}')  # noqa
    finally:
        cursor.cursor.close()
        cursor.connection.close()


def fetch_project_data(
    cursor: CursorWrapper,
    to_fetch: ToFetchProject,
    afs_dict: Dict[int, int],
    orgs_dict: Dict[int, int],
):
    pid = to_fetch.original_project_id
    print(f'Fetching data for deep project {pid}')
    try:
        cursor.execute(queries.projects_q.format(pid))
        data = cursor.fetchall()
        if not data:
            print('no project', pid)
            to_fetch.status = ToFetchProject.FetchStatus.NOT_FOUND
            to_fetch.save()
            return
    except psycopg2.ProgrammingError:
        to_fetch.status = ToFetchProject.FetchStatus.ERRORED
        to_fetch.save()
    else:
        columns = [c.name for c in cursor.description]
        project_dict = dict(zip(columns, data[0]))
        afid = project_dict['analysis_framework_id']
        if afid is not None and afid not in afs_dict:
            to_fetch.status = ToFetchProject.FetchStatus.NOT_FOUND
            to_fetch.error = "Af not found for project"
            to_fetch.save()
            logger.warning(f'Could not find DEEP af with id {afid} and project id {pid}. Skipping.')  # noqa
            print(f'Could not find DEEP af with id {afid} and project id {pid}. Skipping.')  # noqa
            return
        if len(data) == 0:
            logger.warning(f'Could not find DEEP project with id {pid}. Skipping.')  # noqa
            print(f'Could not find DEEP project with id {pid}. Skipping.')  # noqa
            to_fetch.status = ToFetchProject.FetchStatus.NOT_FOUND
            to_fetch.save()
            return
        project, _ = Project.objects.update_or_create(
            original_project_id=to_fetch.original_project_id,
            defaults={
                'af_mapping_id': afs_dict.get(afid),
                'to_fetch_project': to_fetch,
                'title': project_dict['title'],
                'location': '',  # TODO: To discuss what to put in here
                'description': project_dict['description'],
                'extra': {
                    k: str(project_dict[k])
                    for k in ['start_date', 'end_date']
                }
            }
        )
        logger.info(f'Fetched project data for deep project {pid}')
        print(f'Fetched project data for deep project {pid}')

        leads_dict = fetch_project_leads(cursor, project, orgs_dict)
        print('leads_dict', leads_dict)
        if leads_dict:
            fetch_project_entries(cursor, project, leads_dict)

        logger.info(f'Fetched all data for deep project {pid}')
        print(f'Fetched all data for deep project {pid}')
        to_fetch.status = ToFetchProject.FetchStatus.FETCHED
        to_fetch.save()


def _process_lead_batch(lead_batch, project, orgs_dict, columns):
    lead_extra_fields = [
        'author_raw', 'source_raw', 'priority', 'status', 'published_on',
    ]
    lead_dict = {}
    for lead in lead_batch:
        lead_dict = dict(zip(columns, lead))
        auth_id = lead_dict['author_id']
        source_id = lead_dict['source_id']
        Lead.objects.update_or_create(
            original_lead_id=lead_dict['id'],
            defaults={
                'project': project,
                'authoring_org_id': orgs_dict.get(auth_id),
                'publishing_org_id': orgs_dict.get(source_id),
                'title': lead_dict['title'],
                'text_extract': lead_dict['text_extract'],
                'source_url': lead_dict['url'],
                'confidentiality': lead_dict['confidentiality'],
                'extra': {
                    k: str(lead_dict[k])
                    for k in lead_extra_fields
                }
            }
        )
    return lead_dict


def fetch_project_leads(
    cursor: CursorWrapper,
    project: Project,
    orgs_dict: Dict[int, int],
) -> OptDictIntObj[int]:
    pid = project.original_project_id
    print(f'Fetching lead data for deep project {pid}')
    try:
        last_fetched = project.to_fetch_project.last_fetched_lead_created_at
        cursor.execute(queries.lead_q.format(pid, last_fetched or VERY_PAST_DATE))  # noqa
        rows = cursor_fetch_iterator(cursor)
    except psycopg2.ProgrammingError as e:
        logger.warning(f'Error fetching leads for deep project {pid}: {e}')
        print(f'Error fetching leads for deep project {pid}: {e}')
        return
    else:
        columns = []
        # fetched in asc order
        batch_size = 500
        for i, row_batch in enumerate(batched(rows, batch_size)):
            columns = columns if columns else [c.name for c in cursor.description]  # noqa
            with transaction.atomic():
                last_lead_dict = _process_lead_batch(row_batch, project, orgs_dict, columns)  # noqa
                project.to_fetch_project.last_fetched_lead_created_at = last_lead_dict['created_at']  # noqa
                project.to_fetch_project.save()
            print(f'fetched {i+1} batch({batch_size}) of leads')
    print(f'Fetched lead data for deep project {pid}')
    return dict(Lead.objects.values_list('original_lead_id', 'id'))


def _process_entries_batch(entries_batch, leads_dict, columns):
    entry_extra_fields = [
        'information_date', 'entry_type', 'excerpt_modified', 'excerpt'
    ]
    entry_dict = {}
    for row in entries_batch:
        entry_dict = dict(zip(columns, row))
        lead_id = leads_dict.get(entry_dict['lead_id'])
        if lead_id is None:
            continue
        Entry.objects.update_or_create(
            original_entry_id=entry_dict['id'],
            lead_id=lead_id,
            defaults={
                'original_lang': '',  # TODO: fill this
                'excerpt_en': '',  # TODO: fill this
                'excerpt_es': '',  # TODO: fill this
                'excerpt_fr': '',  # TODO: fill this
                'excerpt_pt': '',  # TODO: fill this
                'original_af_tags': {},  # TODO: fill this
                'nlp_af_tags': {},  # TODO: fill this
                'export_data': entry_dict['export_data'],
                'af_exportable_data': entry_dict['af_exportable_data'],
                'extra': {
                    k: entry_dict[k]
                    for k in entry_extra_fields
                }
            }
        )
    return entry_dict


def fetch_project_entries(
    cursor: CursorWrapper,
    project: Project,
    leads_dict: Dict[int, int],
):
    pid = project.original_project_id
    try:
        last_fetched = project.to_fetch_project.last_fetched_entry_created_at
        cursor.execute(
            queries.entries_exportable_q.format(
                pid, last_fetched or VERY_PAST_DATE
            )
        )
        rows = cursor_fetch_iterator(cursor)
    except psycopg2.ProgrammingError as e:
        logger.warning(f'Error fetching entries for deep project {pid}')
        print(f'Error fetching entries for deep project {pid} : {e}')
        return
    else:
        columns = []
        print('fetching entries')
        batch_size = 500
        for i, row_batch in enumerate(batched(rows, batch_size)):
            columns = columns if columns else [c.name for c in cursor.description]
            with transaction.atomic():
                last_entry_dict = _process_entries_batch(
                    row_batch,
                    leads_dict,
                    columns
                )
                to_fetch = project.to_fetch_project
                to_fetch.last_fetched_entry_created_at = last_entry_dict['created_at']
                to_fetch.save()
            print(f'Fetched {i+1} batches({batch_size}) entries')
    print(f'fetched entries for project {pid}')


def fetch_afs(
    cursor: CursorWrapper,
    tracker: DeepDataFetchTracker
) -> OptDictIntObj[int]:
    af_extra_fields = ['description', 'properties']
    try:
        last_fetched = tracker.last_fetched_af_created_at
        # fetched with created at ascending order
        cursor.execute(queries.af_q.format(last_fetched or VERY_PAST_DATE))
        rows = cursor_fetch_iterator(cursor)
    except psycopg2.ProgrammingError as e:
        logger.warning('Error fetching afs: ' + repr(e))
        return
    else:
        columns = []
        for i, row in enumerate(rows):
            columns = columns if columns else [c.name for c in cursor.description]  # noqa
            af_dict = dict(zip(columns, row))
            widgets_data = {
                'widget_ids': af_dict['widget_ids'],
                'widget_titles': af_dict['widget_titles'],
                'widget_properties': af_dict['widget_properties'],
                'widget_versions': af_dict['widget_versions'],
            }
            extra_data = {
                'widgets_data': widgets_data,
                **{
                    k: af_dict[k]
                    for k in af_extra_fields
                }
            }
            with transaction.atomic():
                af_mapping, _ = AFMapping.objects.update_or_create(
                    original_af_id=af_dict['id'],
                    defaults={
                        'af_name': af_dict['title'],
                        'original_af_tags': {},  # TODO: Fill this up
                        'nlp_tags': {},  # TODO: Fill this up
                        'is_mapped_manually': False,  # TODO: find the value
                        'extra': extra_data,
                    }
                )
                if i % 200 == 0:
                    print(f'Inerserted {i+1} af')
                tracker.last_fetched_af_created_at = af_dict['created_at']
                tracker.save()
        print('fetched afs')
        return dict(AFMapping.objects.values_list('original_af_id', 'id'))


def fetch_orgs(
    cursor: CursorWrapper,
    tracker: DeepDataFetchTracker
) -> OptDictIntObj[int]:
    org_extra_fields = ["url", "source", "parent_id", "organization_type"]
    try:
        last_fetched = tracker.last_fetched_org_created_at
        # fetched with created at ascending order
        cursor.execute(queries.org_q.format(last_fetched or VERY_PAST_DATE))
        rows = cursor_fetch_iterator(cursor)
    except psycopg2.ProgrammingError as e:
        logger.warning('Error fetching afs: ' + repr(e))
        return
    else:
        columns = []
        for i, row in enumerate(rows):
            columns = columns if columns else [c.name for c in cursor.description]  # noqa
            org_dict = dict(zip(columns, row))
            with transaction.atomic():
                org, _ = Organization.objects.update_or_create(
                    original_organization_id=org_dict["id"],
                    defaults={
                        "name": org_dict["title"],
                        "short_name": org_dict["short_name"],
                        "long_name": org_dict["long_name"],
                        "extra": {
                            k: org_dict[k]
                            for k in org_extra_fields
                        }
                    },
                )
                tracker.last_fetched_org_created_at = org_dict['created_at']
                tracker.save()
                if i % 200 == 0:
                    print(f'Inerserted {i+1} org')
        print('fetched orgs')
        return dict(
            Organization.objects.values_list('original_organization_id', 'id')
        )
