import psycopg2
from typing import Optional, Dict, TypeVar

from datetime import datetime
from celery import shared_task
from django.db import transaction

from core.tasks import queries
from utils.db import connect_db, cursor_fetch_iterator, CursorWrapper
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

tracker = None


def fetch_deep_data():
    global tracker
    tracker = DeepDataFetchTracker.objects.first()
    if tracker is None:
        tracker = DeepDataFetchTracker.objects.create()
    print('connecting')
    cursor = connect_db()
    print('connected')
    try:
        afs_set = fetch_afs(cursor, tracker)
        orgs_set = fetch_orgs(cursor, tracker)
        if orgs_set is None:
            logger.warning('Could not fetch orgs. Continuing without orgs, some lead fields may be null')  # noqa
        if afs_set is None:
            logger.warning('Could not fetch analysis frameowrks. Exiting.')
            return
        not_fetched = ToFetchProject.FetchStatus.NOT_FETCHED
        for prj in ToFetchProject.objects.filter(status=not_fetched):
            print(f'Fetching deep project with id {prj.original_project_id}')  # noqa
            logger.info(f'Fetching deep project with id {prj.original_project_id}')  # noqa
            fetch_project_data(
                cursor,
                prj,
                afs_set,
                orgs_set or set()
            )
            logger.info(f'Fetched deep project with id {prj.original_project_id}')  # noqa
    finally:
        cursor.cursor.close()
        cursor.connection.close()


def fetch_project_data(
    cursor: CursorWrapper,
    to_fetch: ToFetchProject,
    afs_set: set[int],
    orgs_set: set[int],
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
        if afid is not None and afid not in afs_set:
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
        project = Project(
            original_project_id=to_fetch.original_project_id,
            af_mapping_id=afid,
            to_fetch_project=to_fetch,
            title=project_dict['title'],
            location='',  # TODO: fill this up. To discuss what to put in here
            description=project_dict['description'],
            extra={
                k: str(project_dict[k])
                for k in ['start_date', 'end_date']
            }
        )
        project.save()
        logger.info(f'Fetched data for deep project {pid}')
        print(f'Fetched data for deep project {pid}')
        to_fetch.status = ToFetchProject.FetchStatus.FETCHED
        to_fetch.save()

        leads_set = fetch_project_leads(cursor, project, orgs_set)
        if leads_set is not None:
            fetch_project_entries(cursor, project, leads_set)


# TODO: maybe atomic transaction? I think perhaps not.
def fetch_project_leads(
    cursor: CursorWrapper,
    project: Project,
    orgs_set: set[int],
) -> Optional[set[int]]:
    lead_extra_fields = [
        'author_raw', 'source_raw', 'priority', 'status', 'published_on',
    ]
    pid = project.original_project_id
    print(f'Fetching lead data for deep project {pid}')
    try:
        last_fetched = project.to_fetch_project.last_fetched_lead_created_at
        cursor.execute(queries.lead_q.format(pid, last_fetched or VERY_PAST_DATE))
        rows = cursor_fetch_iterator(cursor)
    except psycopg2.ProgrammingError:
        logger.warning(f'Error fetching leads for deep project {pid}')
        return
    else:
        columns = []
        # fetched in asc order
        for row in rows:
            columns = columns if columns else [c.name for c in cursor.description]
            lead_dict = dict(zip(columns, row))
            auth_id = lead_dict['author_id']
            source_id = lead_dict['source_id']
            with transaction.atomic():
                lead = Lead(
                    project=project,
                    authoring_org_id=auth_id if auth_id in orgs_set else None,
                    publishing_org_id=source_id if source_id in orgs_set else None,
                    original_lead_id=lead_dict['id'],
                    title=lead_dict['title'],
                    text_extract=lead_dict['text_extract'],
                    source_url=lead_dict['url'],
                    confidentiality=lead_dict['confidentiality'],
                    extra={
                        k: str(lead_dict[k])
                        for k in lead_extra_fields
                    }
                )
                lead.save()
                project.to_fetch_project.last_fetched_lead_created_at = lead_dict['created_at']
                project.to_fetch_project.save()
    print(f'Fetched lead data for deep project {pid}')
    return set(Lead.objects.values_list('id'))


# TODO: maybe atomic transaction? I think perhaps not.
def fetch_project_entries(
    cursor: CursorWrapper,
    project: Project,
    leads_set: set[int],
):
    pid = project.original_project_id
    entry_extra_fields = [
        'information_date', 'entry_type', 'excerpt_modified', 'excerpt'
    ]
    try:
        last_fetched = project.to_fetch_project.last_fetched_entry_created_at
        cursor.execute(queries.lead_q.format(pid, last_fetched or VERY_PAST_DATE))
        rows = cursor_fetch_iterator(cursor)
    except psycopg2.ProgrammingError:
        logger.warning(f'Error fetching entries for deep project {pid}')
        return
    else:
        columns = []
        for row in rows:
            columns = columns if columns else [c.name for c in cursor.description]
            entry_dict = dict(zip(columns, row))
            lead_id = entry_dict['lead_id']
            if lead_id not in leads_set:
                continue
            with transaction.atomic():
                Entry.objects.create(
                    original_entry_id=entry_dict['id'],
                    lead_id=lead_id,
                    original_lang='',  # TODO: fill this
                    excerpt_en='',  # TODO: fill this
                    excerpt_es='',  # TODO: fill this
                    excerpt_fr='',  # TODO: fill this
                    excerpt_pt='',  # TODO: fill this
                    original_af_tags={},  # TODO: fill this
                    nlp_af_tags={},  # TODO: fill this
                    extra={
                        k: entry_dict[k]
                        for k in entry_extra_fields
                    }
                )
                project.to_fetch_project.last_fetched_entry_created_at = entry_dict['created_at']
                project.to_fetch_project.save()
    print(f'fetched entries for project {pid}')


def fetch_afs(cursor: CursorWrapper, tracker: DeepDataFetchTracker) -> Optional[set[int]]:
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
        return set(AFMapping.objects.values_list('id'))


def fetch_orgs(cursor: CursorWrapper, tracker: DeepDataFetchTracker) -> Optional[set[int]]:
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
        return set(Organization.objects.values_list('id'))
