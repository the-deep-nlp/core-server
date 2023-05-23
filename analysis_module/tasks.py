from datetime import timedelta
from celery import shared_task

from django.db.models import Q
from django.utils import timezone

from core.models import NLPRequest
from core_server.settings import (
    CRON_RESEND_ECS_REQUEST_MINUTES,
    ECS_REQUESTS_BATCH_SIZE,
    MAX_NLP_PROCESSING_ATTEMPTS,
)
from .utils import send_ecs_http_request


@shared_task
def process_pending_nlp_requests():
    """
    NOTE: This function needs to be run on certain intervals
    This function gets NLPRequests objects whose status is pending and based on
    the type of request, sends appropriate requests to the endpoints.
    """
    now = timezone.now()
    lookup_before = now - timedelta(minutes=CRON_RESEND_ECS_REQUEST_MINUTES)
    to_process_requests = NLPRequest.objects.filter(
        Q(last_process_attempted=None) | Q(last_process_attempted__lte=lookup_before),
        status=NLPRequest.RequestStatus.INITIATED,
        process_attempts__lt=MAX_NLP_PROCESSING_ATTEMPTS,
    )[:ECS_REQUESTS_BATCH_SIZE]
    for req in to_process_requests:
        send_ecs_http_request(req)
        req.process_attempts += 1
        req.last_process_attempted = timezone.now()
        req.save(update_fields=["process_attempts", "last_process_attempted"])
