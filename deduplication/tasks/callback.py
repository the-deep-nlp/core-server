import requests
import traceback
from typing import Tuple, Optional
from celery import shared_task
from celery.utils.log import get_task_logger
from django.db import transaction

from core.models import Lead
from utils.transformations import serialize_minhash
from deduplication.models import DeduplicationRequest, LSHIndex, LeadHash
from deduplication.utils import get_minhash, insert_to_index

logger = get_task_logger(__name__)


RequestStatus = DeduplicationRequest.RequestStatus


def create_lead_and_update_index(dedup_req: DeduplicationRequest, lsh_index: LSHIndex):
    lead_object, created = Lead.objects.get_or_create(
        original_lead_id=dedup_req.lead_id,
        defaults={
            "project": lsh_index.project,
            "text_extract": dedup_req.text_extract,
        },
    )
    lead_hash = get_minhash(dedup_req.text_extract)
    lead_hash_obj, created = LeadHash.objects.get_or_create(
        lead=lead_object,
        lsh_index=lsh_index,
        defaults={
            "lead_hash": serialize_minhash(lead_hash),
        },
    )
    # insert to index, if lead is created(which means it has not been indexed)
    if created:
        insert_to_index(lsh_index.index, dedup_req.lead_id, lead_hash)

    duplicate_lead_ids = lsh_index.index.query(lead_hash)
    dedup_req.result = {
        "duplicate_lead_ids": duplicate_lead_ids,
    }
    dedup_req.status = RequestStatus.CALCULATED
    dedup_req.save()


@shared_task
def process_dedup_request(dedup_pk: int):
    dedup_req: Optional[DeduplicationRequest] = DeduplicationRequest.objects.filter(
        pk=dedup_pk
    ).first()
    if dedup_req is None:
        logger.warning(f"Could not find deduplication request with pk {dedup_pk}")
        return
    if dedup_req.status != DeduplicationRequest.RequestStatus.PENDING:
        logger.warning("Already processed deduplication request received")
        return

    lsh_index = LSHIndex.objects.filter(
        project__original_project_id=dedup_req.project_id
    ).first()

    if lsh_index is None:
        logger.warning(
            f"LSH Index corresponding to project {dedup_req.project_id} not found."
        )
        return

    if lsh_index.status == LSHIndex.IndexStatus.CREATING:
        logger.warning(
            f"LSH Index is still being created for project {dedup_req.project_id}."
        )
        return

    try:
        with transaction.atomic():
            create_lead_and_update_index(dedup_req, lsh_index)
    except Exception:
        msg = "Error creating lead and updating index for dedup request {dedup_req.id}"
        logger.error(msg, exc_info=True)
        dedup_req.has_errored = True
        dedup_req.error = f"{msg}:\n{traceback.format_exc()}"
        dedup_req.save(update_fields=["has_errored", "error"])

    # Send to DEEP
    success, err = respond_to_deep(dedup_req)
    if not success:
        dedup_req.has_errored = True
        dedup_req.error = err
    else:
        dedup_req.status = RequestStatus.RESPONDED

    dedup_req.save(update_fields=["has_errored", "error", "status"])


def respond_to_deep(dedup_req: DeduplicationRequest) -> Tuple[bool, Optional[str]]:
    try:
        data = {
            "lead_id": dedup_req.lead_id,
            "client_id": dedup_req.client_id,
            "duplicate_lead_ids": dedup_req.result["duplicate_lead_ids"],
        }
    except KeyError:
        return (
            False,
            "Result does not contain appropriate key(duplicate_lead_ids)",
        )

    try:
        resp = requests.post(dedup_req.callback_url, data=data)
    except Exception:
        logger.error("Could not respond to deep", exc_info=True)
        return False, traceback.format_exc()

    if resp.status_code >= 300 or resp.status_code < 200:
        return False, resp.text
    return True, None


@shared_task
def process_dedup_requests():
    dedup_reqs = DeduplicationRequest.objects.filter(
        status=DeduplicationRequest.RequestStatus.PENDING
    )
    for req in dedup_reqs:
        process_dedup_request(req.pk)
