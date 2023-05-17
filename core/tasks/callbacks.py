from datetime import datetime, timedelta
from celery import shared_task

from core.models import FailedCallback


def get_failed_callbacks():
    now = datetime.now()
    one_day_before = now - timedelta(hours=24)
    return FailedCallback.objects.filter(
        status=FailedCallback.Status.RETRYING,
        created_at__gte=one_day_before,
    )


@shared_task(name="core.tasks.resend_failed_callbacks")
def resend_failed_callbacks():
    failed_callbacks = get_failed_callbacks()
    for failed_callback in failed_callbacks:
        failed_callback.resend_callback_request()
