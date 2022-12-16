import requests
import traceback
from typing import Tuple, Optional
from celery import shared_task
from celery.utils.log import get_task_logger

from utils.transformations import serialize_minhash
from deduplication.models import DeduplicationRequest, LSHIndex
from deduplication.utils import get_minhash

logger = get_task_logger(__name__)


RequestStatus = DeduplicationRequest.RequestStatus


@shared_task
def process_dedup_request(dedup_pk: int):
    dedup_req: Optional[DeduplicationRequest] = DeduplicationRequest.objects.filter(
        pk=dedup_pk
    ).first()
    if dedup_req is None:
        logger.warning(
            f"Could not find deduplication request with pk {dedup_pk}"
        )
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

    try:
        lead_hash = get_minhash(dedup_req.text_extract)
        duplicate_lead_ids = lsh_index.index.query(lead_hash)
        dedup_req.result = {
            "duplicate_lead_ids": duplicate_lead_ids,
        }
    except Exception:
        dedup_req.has_errored = True
        dedup_req.error = f"StackTrace:\n{traceback.format_exc()}"
        dedup_req.save(update_fields=['has_errored', 'error'])

    dedup_req.status = RequestStatus.CALCULATED
    dedup_req.save(update_fields=['status', 'result'])

    # Send to DEEP
    success, err = respond_to_deep(dedup_req)
    if not success:
        dedup_req.has_errored = True
        dedup_req.error = err
    else:
        dedup_req.status = RequestStatus.RESPONDED

    dedup_req.save(update_fields=['has_errored', 'error', 'status'])

    # Update index


def respond_to_deep(dedup_req: DeduplicationRequest) -> Tuple[bool, Optional[str]]:
    try:
        data = {
            "lead_id": dedup_req.lead_id,
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
        return False, traceback.format_exc()

    if resp.status_code >= 300 or resp.status_code < 200:
        return False, resp.text
    return True, None
