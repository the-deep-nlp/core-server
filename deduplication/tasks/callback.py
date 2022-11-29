import requests

from celery import shared_task
from celery.utils.log import get_task_logger

from deduplication.models import DeduplicationRequest

logger = get_task_logger(__name__)


@shared_task
def process_dedup_request(dedup_request_pk: int):
    pass
