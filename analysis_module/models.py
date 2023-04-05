import uuid
from django.db import models


class AnalysisModuleRequest(models.Model):

    class RequestStatus(models.IntegerChoices):
        INITIATED = 1
        SUCCESS = 2
        FAILED = 3
        PROCESS_INPUT_URL_FAILED = 4

    class FeaturesType(models.TextChoices):
        NGRAMS = "ngrams", "Ngrams"
        TOPICMODEL = "topicmodel", "Topicmodel"
        SUMMARIZATION = "summarization", "Summarization"

    client_id = models.CharField(max_length=50)
    status = models.IntegerField(choices=RequestStatus.choices, default=RequestStatus.INITIATED)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    result_s3_link = models.URLField(null=True, blank=True)
    type = models.CharField(choices=FeaturesType.choices, max_length=20)
    request_params = models.JSONField(null=True, blank=True)  # To capture the original request params
    error = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "event_status_tracker"
