import pickle
from datasketch import MinHashLSH
from django.db import transaction
from django.db.models import QuerySet
from celery import shared_task
from celery.utils.log import get_task_logger

from utils.decorators import log_time
from utils.transformations import batched, serialize_minhash
from core.models import Lead, Project, ToFetchProject
from deduplication.models import LSHIndex, LeadHash
from deduplication.utils import get_minhash, insert_to_index

logger = get_task_logger(__name__)


def _process_and_insert_lead(lead: Lead, index_obj: LSHIndex, index: MinHashLSH):
    minhash = get_minhash(lead.text_extract)
    insert_to_index(index, lead.original_lead_id, minhash)
    LeadHash.objects.update_or_create(
        lead=lead,
        lsh_index=index_obj,
        defaults={
            "lead_hash": serialize_minhash(minhash),
        },
    )


def process_and_insert_leads(
    project: Project,
    leads: QuerySet[Lead],
    index_obj: LSHIndex,
    index: MinHashLSH,
):
    try:
        batches = batched(leads, batch_size=200)
        for i, batch in enumerate(batches):
            with transaction.atomic():
                for lead in batch:
                    _process_and_insert_lead(lead, index_obj, index)
            logger.info("processed batch", i)
    except Exception:
        logger.warning(
            f"Error creating index for project {project.original_project_id}"
        )
        import traceback

        index_obj.has_errored = True
        index_obj.error = traceback.format_exc()
        index_obj.save()
    else:
        # Update the index
        index_obj.index = index
        index_obj.status = LSHIndex.IndexStatus.CREATED
        index_obj.save()


def create_project_index(project: Project):
    index_obj, created = LSHIndex.objects.get_or_create(
        project=project,
        defaults={
            "name": project.title,
            "pickle_version": pickle.format_version,
        },
    )
    if index_obj.has_errored:
        return
    # Fetch leads which have been extracted and whose hash does not exist
    leads = Lead.objects.filter(
        project=project,
        text_extract__isnull=False,
        leadhash__isnull=True,
    )
    if created:
        index = MinHashLSH(
            threshold=LSHIndex.THRESHOLD,
            num_perm=LSHIndex.NUM_PERM,
        )
    else:
        index = index_obj.index

    process_and_insert_leads(project, leads, index_obj, index)


@shared_task
def create_indices():
    all_projects = Project.objects.filter(
        to_fetch_project__status=ToFetchProject.FetchStatus.FETCHED
    )
    for project in all_projects:
        with log_time(f'Indexing project({project.id}) "{project.title}"'):
            create_project_index(project)
