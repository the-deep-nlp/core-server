import uuid
import requests
from datetime import datetime

from django.db import models
from django.contrib.postgres.fields import ArrayField

from core_server.settings import CALLBACK_MAX_RETRIES_LIMIT
from core_server.base_models import BaseModel

import logging

logger = logging.getLogger(__name__)


class DeepDataFetchTracker(BaseModel):
    last_fetched_org_created_at = models.DateTimeField(null=True, blank=True)
    last_fetched_af_created_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.pk is None and DeepDataFetchTracker.objects.first() is not None:  # noqa
            raise Exception("Cannot create multiple trackers")
        super().save(*args, **kwargs)


class ToFetchProject(BaseModel):
    """This model keeps track of the projects whose data needs to be fetched.
    Also keeps track of last leads and entries fetched
    """

    class FetchStatus(models.TextChoices):
        NOT_FETCHED = "not_fetched", "Not Fetched"
        FETCHING = "fetching", "Fetching"
        FETCHED = "fetched", "Fetched"
        ERRORED = "errored", "Errored"
        NOT_FOUND = "not_found", "Not Found"

    class ActiveStatus(models.TextChoices):
        ACTIVE = 'active'
        INACTIVE = 'inactive'

    original_project_id = models.PositiveIntegerField(unique=True)
    active_status = models.CharField(
        max_length=20,
        choices=ActiveStatus.choices,
        default=ActiveStatus.ACTIVE,
    )
    status = models.CharField(
        max_length=20,
        choices=FetchStatus.choices,
        default=FetchStatus.NOT_FETCHED,
    )
    last_fetched_lead_created_at = models.DateTimeField(null=True, blank=True)
    last_fetched_entry_created_at = models.DateTimeField(null=True, blank=True)
    """
    is_added_manually:
    There are two ways this object is added: one when user manually adds it and the other
    when some request(for eg: dedup) from DEEP requires the project data to be fetched.
    For example: User might want to fetch project data(leads, entries, etc) for other nlp tasks.
    However DEEP might send dedup request for a lead in a project that is not yet in nlp server.
    In later case too, we need to have ToFetchProject object added as DEEP data is fetched based
    on this object.
    is_added_manually just distinguishes how this object was added.
    """
    is_added_manually = models.BooleanField(default=True)
    error = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.original_project_id)


class Organization(BaseModel):
    original_organization_id = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255)
    long_name = models.CharField(max_length=255)
    extra = models.JSONField()

    def __str__(self):
        return self.name


class AFMapping(BaseModel):
    af_name = models.CharField(max_length=200)
    original_af_id = models.PositiveIntegerField(unique=True)
    original_af_tags = models.JSONField(default=dict)
    nlp_tags = models.JSONField(default=dict)
    is_mapped_manually = models.BooleanField()
    extra = models.JSONField(default=dict)

    def __str__(self):
        return self.af_name


class Project(BaseModel):
    original_project_id = models.PositiveIntegerField(unique=True)
    af_mapping = models.ForeignKey(AFMapping, null=True, on_delete=models.CASCADE)
    to_fetch_project = models.ForeignKey(
        ToFetchProject,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    extra = models.JSONField(default=dict)

    def __str__(self):
        return self.title


class Lead(BaseModel):
    class Confidentiality(models.TextChoices):
        UNPROTECTED = "unprotected", "Public"
        RESTRICTED = "restricted", "Restricted"
        CONFIDENTIAL = "confidential", "Confidential"

    class ExtractionStatus(models.IntegerChoices):
        PENDING = 0, "Pending"
        STARTED = 1, "Started"
        RETRYING = 4, "Retrying"
        SUCCESS = 2, "Success"
        FAILED = 3, "Failed"

    original_lead_id = models.PositiveIntegerField(unique=True)
    title = models.CharField(max_length=255)
    extraction_status = models.SmallIntegerField(
        choices=ExtractionStatus.choices, default=ExtractionStatus.PENDING
    )
    text_extract = models.TextField(null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    authoring_org = models.ForeignKey(
        Organization,
        null=True,
        on_delete=models.CASCADE,
        related_name="authored_leads",
    )
    publishing_org = models.ForeignKey(
        Organization,
        null=True,
        on_delete=models.CASCADE,
        related_name="published_leads",
    )
    confidentiality = models.CharField(
        max_length=30,
        choices=Confidentiality.choices,
        default=Confidentiality.UNPROTECTED,
    )
    source_url = models.TextField()
    extra = models.JSONField(default=dict)

    def __str__(self):
        return self.text_extract[:50] if self.text_extract else "-- Not extracted --"


class Entry(BaseModel):
    original_entry_id = models.PositiveIntegerField(unique=True)
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    original_lang = models.CharField(max_length=50)
    excerpt = models.TextField()
    # original_af_tags contains the labels manually tagged by the taggers.
    # The structure is shown after the fields declaration below
    original_af_tags = models.JSONField(default=dict)
    export_data = models.JSONField(default=dict)
    extra = models.JSONField(default=dict)
    deep_entry_created_at = models.DateTimeField()

    nlp_tags = models.JSONField(default=list)
    nlp_mapping = models.JSONField(default=dict)

    """
    NOTE:
    original_af_tags = {
        "sectors": ["xXx"],             # might not be present
        "subpillars_1d": ["xXx"],       # might not be present
        "subpillars_2d": ["xXx"],       # might not be present
    }
    """

    # It's no more like above but something like the following:
    # for now, the date widget has been excluded (idk if related with created_at
    # or a data that the analyst assign to the excerpt) and the mapped
    # geolocations too. We already have the information in original_af_tags

    """
    NOTE:
    original_af_tags = {
        'matrix2dWidget': ['protection', 'impact->impact on people'],
        'geoWidget': [659709, 659702],
        'scaleWidget': ['usually reliable'],
        'matrix1dWidget': ['conflict->casualties & missings'],
        'dateRangeWidget': ['04-03-2022']
    }

    nlp_tags = [
        'first_level_tags->pillars_2d->Impact',
        'subpillars_2d->Impact->Impact on people',
        'first_level_tags->sectors->Protection',
        'secondary_tags->reliability->Usually reliable',
        'first_level_tags->pillars_1d->Casualties'
    ]

    nlp_mapping = {
        'protection': ['first_level_tags->sectors->Protection'],
        'impact->impact on people': ['subpillars_2d->Impact->Impact on people',
        'first_level_tags->pillars_2d->Impact'],
        'usually reliable': ['secondary_tags->reliability->Usually reliable'],
        'conflict->casualties & missings': ['first_level_tags->pillars_1d->Casualties']
    }
    """

    def __str__(self):
        return f"Original entry {self.original_entry_id}"


class ClassificationModel(BaseModel):
    name = models.CharField(max_length=200)
    version = models.CharField(max_length=20)
    model_uri = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    train_data_uri = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = ['name', 'version', 'model_uri']

    def __str__(self):
        return f"{self.name}-{self.id}"


class ClassificationPredictions(BaseModel):
    entry = models.OneToOneField(Entry, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    model = models.ForeignKey(ClassificationModel, on_delete=models.CASCADE)
    embeddings = ArrayField(models.FloatField(blank=True), blank=True, null=True)
    subpillars_1d = ArrayField(
        models.CharField(max_length=500, blank=True),
        default=list,
    )
    sectors = ArrayField(
        models.CharField(max_length=500, blank=True), default=list,
    )
    subpillars_2d = ArrayField(
        models.CharField(max_length=500, blank=True), default=list,
    )
    age = ArrayField(
        models.CharField(max_length=500, blank=True), default=list,
    )
    gender = ArrayField(
        models.CharField(max_length=500, blank=True), default=list,
    )
    affected_groups = ArrayField(
        models.CharField(max_length=500, blank=True), default=list,
    )
    specific_needs_groups = ArrayField(
        models.CharField(max_length=500, blank=True), default=list,
    )
    severity = ArrayField(
        models.CharField(max_length=500, blank=True), default=list,
    )

    def __str__(self):
        return str(self.entry.original_entry_id)


class ProjectWisePerfMetrics(models.Model):
    project_id = models.PositiveIntegerField()  # project_id from deep
    sectors_f1score = models.FloatField(blank=True, null=True)
    sectors_precision = models.FloatField(blank=True, null=True)
    sectors_recall = models.FloatField(blank=True, null=True)
    subpillars_1d_f1score = models.FloatField(blank=True, null=True)
    subpillars_1d_precision = models.FloatField(blank=True, null=True)
    subpillars_1d_recall = models.FloatField(blank=True, null=True)
    subpillars_2d_f1score = models.FloatField(blank=True, null=True)
    subpillars_2d_precision = models.FloatField(blank=True, null=True)
    subpillars_2d_recall = models.FloatField(blank=True, null=True)
    pillars_1d_f1score = models.FloatField(blank=True, null=True)
    pillars_1d_precision = models.FloatField(blank=True, null=True)
    pillars_1d_recall = models.FloatField(blank=True, null=True)
    pillars_2d_f1score = models.FloatField(blank=True, null=True)
    pillars_2d_precision = models.FloatField(blank=True, null=True)
    pillars_2d_recall = models.FloatField(blank=True, null=True)
    age_f1score = models.FloatField(blank=True, null=True)
    age_precision = models.FloatField(blank=True, null=True)
    age_recall = models.FloatField(blank=True, null=True)
    displaced_f1score = models.FloatField(blank=True, null=True)
    displaced_precision = models.FloatField(blank=True, null=True)
    displaced_recall = models.FloatField(blank=True, null=True)
    gender_f1score = models.FloatField(blank=True, null=True)
    gender_precision = models.FloatField(blank=True, null=True)
    gender_recall = models.FloatField(blank=True, null=True)
    non_displaced_f1score = models.FloatField(blank=True, null=True)
    non_displaced_precision = models.FloatField(blank=True, null=True)
    non_displaced_recall = models.FloatField(blank=True, null=True)
    severity_f1score = models.FloatField(blank=True, null=True)
    severity_precision = models.FloatField(blank=True, null=True)
    severity_recall = models.FloatField(blank=True, null=True)
    specific_needs_groups_f1score = models.FloatField(blank=True, null=True)
    specific_needs_groups_precision = models.FloatField(blank=True, null=True)
    specific_needs_groups_recall = models.FloatField(blank=True, null=True)
    affected_f1score = models.FloatField(blank=True, null=True)
    affected_precision = models.FloatField(blank=True, null=True)
    affected_recall = models.FloatField(blank=True, null=True)

    generated_at = models.DateTimeField()

    def __str__(self):
        return str(self.project_id)


class TagWisePerfMetrics(models.Model):
    tags = models.CharField(max_length=250, blank=True)
    generated_at = models.DateTimeField()
    score = models.FloatField(blank=True, null=True)
    metric = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.tags


class AllProjectPerfMetrics(models.Model):
    category = models.CharField(max_length=250, blank=True)
    precision = models.FloatField(blank=True, null=True)
    recall = models.FloatField(blank=True, null=True)
    f1score = models.FloatField(blank=True, null=True)
    support = models.FloatField(blank=True, null=True)
    generated_at = models.DateTimeField()

    def __str__(self):
        return self.category


class CategoryWiseMatchRatios(models.Model):
    sectors_completely_matched = models.FloatField(blank=True, null=True)
    sectors_missing = models.FloatField(blank=True, null=True)
    sectors_wrong = models.FloatField(blank=True, null=True)
    pillars_1d_completely_matched = models.FloatField(blank=True, null=True)
    pillars_1d_missing = models.FloatField(blank=True, null=True)
    pillars_1d_wrong = models.FloatField(blank=True, null=True)
    pillars_2d_completely_matched = models.FloatField(blank=True, null=True)
    pillars_2d_missing = models.FloatField(blank=True, null=True)
    pillars_2d_wrong = models.FloatField(blank=True, null=True)
    subpillars_1d_completely_matched = models.FloatField(blank=True, null=True)
    subpillars_1d_missing = models.FloatField(blank=True, null=True)
    subpillars_1d_wrong = models.FloatField(blank=True, null=True)
    subpillars_2d_completely_matched = models.FloatField(blank=True, null=True)
    subpillars_2d_missing = models.FloatField(blank=True, null=True)
    subpillars_2d_wrong = models.FloatField(blank=True, null=True)
    age_completely_matched = models.FloatField(blank=True, null=True)
    age_missing = models.FloatField(blank=True, null=True)
    age_wrong = models.FloatField(blank=True, null=True)
    displaced_completely_matched = models.FloatField(blank=True, null=True)
    displaced_missing = models.FloatField(blank=True, null=True)
    displaced_wrong = models.FloatField(blank=True, null=True)
    gender_completely_matched = models.FloatField(blank=True, null=True)
    gender_missing = models.FloatField(blank=True, null=True)
    gender_wrong = models.FloatField(blank=True, null=True)
    non_displaced_completely_matched = models.FloatField(blank=True, null=True)
    non_displaced_missing = models.FloatField(blank=True, null=True)
    non_displaced_wrong = models.FloatField(blank=True, null=True)
    severity_completely_matched = models.FloatField(blank=True, null=True)
    severity_missing = models.FloatField(blank=True, null=True)
    severity_wrong = models.FloatField(blank=True, null=True)
    specific_needs_groups_completely_matched = models.FloatField(blank=True, null=True)
    specific_needs_groups_missing = models.FloatField(blank=True, null=True)
    specific_needs_groups_wrong = models.FloatField(blank=True, null=True)
    affected_completely_matched = models.FloatField(blank=True, null=True)
    affected_missing = models.FloatField(blank=True, null=True)
    affected_wrong = models.FloatField(blank=True, null=True)
    entry_id = models.PositiveIntegerField()  # entry id from deep
    project_id = models.PositiveIntegerField()  # project id from deep
    generated_at = models.DateTimeField()

    def __str__(self):
        return str(self.entry_id)


class ProjectWiseMatchRatios(models.Model):
    project_id = models.PositiveIntegerField()  # project id from deep
    sectors_completely_matched_mean = models.FloatField(blank=True, null=True)
    sectors_missing_mean = models.FloatField(blank=True, null=True)
    sectors_wrong_mean = models.FloatField(blank=True, null=True)
    pillars_1d_completely_matched_mean = models.FloatField(blank=True, null=True)
    pillars_1d_missing_mean = models.FloatField(blank=True, null=True)
    pillars_1d_wrong_mean = models.FloatField(blank=True, null=True)
    pillars_2d_completely_matched_mean = models.FloatField(blank=True, null=True)
    pillars_2d_missing_mean = models.FloatField(blank=True, null=True)
    pillars_2d_wrong_mean = models.FloatField(blank=True, null=True)
    subpillars_1d_completely_matched_mean = models.FloatField(blank=True, null=True)
    subpillars_1d_missing_mean = models.FloatField(blank=True, null=True)
    subpillars_1d_wrong_mean = models.FloatField(blank=True, null=True)
    subpillars_2d_completely_matched_mean = models.FloatField(blank=True, null=True)
    subpillars_2d_missing_mean = models.FloatField(blank=True, null=True)
    subpillars_2d_wrong_mean = models.FloatField(blank=True, null=True)
    age_completely_matched_mean = models.FloatField(blank=True, null=True)
    age_missing_mean = models.FloatField(blank=True, null=True)
    age_wrong_mean = models.FloatField(blank=True, null=True)
    displaced_completely_matched_mean = models.FloatField(blank=True, null=True)
    displaced_missing_mean = models.FloatField(blank=True, null=True)
    displaced_wrong_mean = models.FloatField(blank=True, null=True)
    gender_completely_matched_mean = models.FloatField(blank=True, null=True)
    gender_missing_mean = models.FloatField(blank=True, null=True)
    gender_wrong_mean = models.FloatField(blank=True, null=True)
    non_displaced_completely_matched_mean = models.FloatField(blank=True, null=True)
    non_displaced_missing_mean = models.FloatField(blank=True, null=True)
    non_displaced_wrong_mean = models.FloatField(blank=True, null=True)
    severity_completely_matched_mean = models.FloatField(blank=True, null=True)
    severity_missing_mean = models.FloatField(blank=True, null=True)
    severity_wrong_mean = models.FloatField(blank=True, null=True)
    specific_needs_groups_completely_matched_mean = models.FloatField(blank=True, null=True)
    specific_needs_groups_missing_mean = models.FloatField(blank=True, null=True)
    specific_needs_groups_wrong_mean = models.FloatField(blank=True, null=True)
    affected_completely_matched_mean = models.FloatField(blank=True, null=True)
    affected_missing_mean = models.FloatField(blank=True, null=True)
    affected_wrong_mean = models.FloatField(blank=True, null=True)
    generated_at = models.DateTimeField()

    def __str__(self):
        return str(self.project_id)


class ComputedFeatureDrift(models.Model):
    reference_project_id = models.PositiveIntegerField()
    current_project_id = models.PositiveIntegerField()
    reference_dataset_len = models.PositiveIntegerField(blank=True, null=True)
    current_dataset_len = models.PositiveIntegerField(blank=True, null=True)
    drift_share = models.BooleanField()
    number_of_columns = models.PositiveIntegerField(blank=True, null=True)
    number_of_drifted_columns = models.PositiveIntegerField(blank=True, null=True)
    share_of_drifted_columns = models.FloatField(blank=True, null=True)
    dataset_drift = models.BooleanField()
    generated_at = models.DateTimeField()
    entry_count = models.PositiveIntegerField(blank=True, default=0)

    def __str__(self):
        return str(self.reference_project_id)


class NLPRequest(BaseModel):
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
        SUMMARIZATION_V2 = "summarization-v2", "Summarization-V2"
        GEOLOCATION = "geolocation", "Geolocation"
        TAGS_MAPPING = "tags-mapping", "Tags Mapping"
        ENTRY_CLASSIFICATION = "entry-classification", "Entry Classification"
        TEXT_EXTRACTION = "text-extraction", "Text Extraction"

    client_id = models.CharField(max_length=50)
    status = models.IntegerField(choices=RequestStatus.choices, default=RequestStatus.INITIATED)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    result_data = models.JSONField(default=dict)
    type = models.CharField(choices=FeaturesType.choices, max_length=20)
    # To capture the original request params
    request_params = models.JSONField(null=True, blank=True)
    process_attempts = models.PositiveIntegerField(default=0)
    last_process_attempted = models.DateTimeField(null=True)

    class Meta:
        db_table = "event_status_tracker"


class FailedCallback(BaseModel):
    class Status(models.IntegerChoices):
        SUCCESS = 0, "Success"
        RETRY_MAXED_OUT = 1, "Retries maxed out"
        FAILED = 2, "Failed"
        RETRYING = 3, "Retrying"

    # This contains the uuid of NLPRequest object
    request_unique_id = models.UUIDField(unique=True)
    retries_count = models.PositiveIntegerField(default=0)
    last_retried_at = models.DateTimeField(null=True)
    status = models.PositiveIntegerField(
        choices=Status.choices,
        default=Status.RETRYING,
    )

    class Meta:
        db_table = "failed_callback_tracker"

    def resend_callback_request(self):
        if self.retries_count >= CALLBACK_MAX_RETRIES_LIMIT:
            self.status = self.Status.RETRY_MAXED_OUT
            self.save()
            return
        original_request = NLPRequest.objects.filter(
            unique_id=self.request_unique_id
        ).first()
        if original_request is None:
            self.status = self.Status.FAILED
            self.save()
            return
        callback_url = original_request.request_params and \
            original_request.request_params.get("callback_url")
        if not callback_url:
            self.status = self.Status.FAILED
            self.save()
            return
        try:
            resp = requests.post(callback_url, json=original_request.result_data)
            if resp.ok:
                self.status = self.Status.SUCCESS
                self.last_retried_at = datetime.now()
                self.save()
                return
        except Exception:
            logger.error("Failed callback", exc_info=True)
        self.last_retried_at = datetime.now()
        self.retries_count += 1
        self.save()
