import uuid
from django.db import models


class AnalysisModuleRequest(models.Model):

    class RequestStatus(models.IntegerChoices):
        INITIATED = 1
        SUCCESS = 2
        FAILED = 3

    class FeaturesType(models.TextChoices):
        NGRAMS = "ngrams", "Ngrams"
        TOPICMODEL = "topicmodel", "Topicmodel"
        SUMMARIZATION = "summarization", "Summarization" 

    status = models.IntegerField(choices=RequestStatus.choices, default=RequestStatus.INITIATED)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    result_s3_link = models.URLField()
    type = models.CharField(choices=FeaturesType.choices, max_length=20)

    class Meta:
        db_table = "event_status_tracker"
