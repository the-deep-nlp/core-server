import requests
from datetime import datetime
import uuid
from django.db import models
from core_server.settings import CALLBACK_MAX_RETRIES_LIMIT

import logging

logger = logging.getLogger(__name__)


from core_server.base_models import BaseModel


class AnalysisModuleRequest(BaseModel):
    class RequestStatus(models.IntegerChoices):
        # NOTE: If changed here, corresponding values should be changed in DEEP as well.
        INITIATED = 1
        SUCCESS = 2
        FAILED = 3
        PROCESS_INPUT_URL_FAILED = 4

    class FeaturesType(models.TextChoices):
        NGRAMS = "ngrams", "Ngrams"
        TOPICMODEL = "topicmodel", "Topicmodel"
        SUMMARIZATION = "summarization", "Summarization"
        GEOLOCATION = "geolocation", "Geolocation"

    client_id = models.CharField(max_length=50)
    status = models.IntegerField(choices=RequestStatus.choices, default=RequestStatus.INITIATED)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    result_s3_link = models.TextField(null=True, blank=True)
    type = models.CharField(choices=FeaturesType.choices, max_length=20)
    request_params = models.JSONField(null=True, blank=True)  # To capture the original request params

    class Meta:
        db_table = "event_status_tracker"


class FailedCallback(BaseModel):
    class FailedStatus(models.IntegerChoices):
        SUCCESS = 0, "Success"
        RETRY_MAXED_OUT = 1, "Retries maxed out"
        FAILED = 2, "Failed"
        RETRYING = 3, "Retrying"

    # This contains the uuid of AnalysisModuleRequest object
    request_unique_id = models.UUIDField(unique=True)
    retries_count = models.PositiveIntegerField(default=0)
    last_retried_at = models.DateTimeField(null=True)
    status = models.PositiveIntegerField(
        choices=FailedStatus.choices,
        default=FailedStatus.RETRYING,
    )

    class Meta:
        db_table = "failed_callback_tracker"

    def resend_request(self):
        if self.retries_count >= CALLBACK_MAX_RETRIES_LIMIT:
            self.status = self.FailedStatus.RETRY_MAXED_OUT
            self.save()
            return
        original_request = AnalysisModuleRequest.objects.filter(
            unique_id=self.request_unique_id
        ).first()
        if original_request is None:
            self.status = self.FailedStatus.FAILED
            self.save()
            return
        request_data = {
            "client_id": original_request.unique_id,
            "status": original_request.status,
            "presigned_s3_url": original_request.result_s3_link,
        }
        callback_url = original_request.request_params and \
            original_request.request_params.get("callback_url")
        if not callback_url:
            self.status = self.FailedStatus.FAILED
            self.save()
            return
        try:
            resp = requests.post(callback_url, json=request_data)
            if resp.ok:
                self.status = self.FailedStatus.SUCCESS
                self.last_retried_at = datetime.now()
                self.save()
                return
        except Exception:
            logger.error("Failed callback", exc_info=True)
        self.last_retried_at = datetime.now()
        self.retries_count += 1
        self.save()
