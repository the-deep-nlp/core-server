from django.db import models
from django.contrib.postgres.fields import ArrayField

from core_server.base_models import BaseModel


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

    original_project_id = models.PositiveIntegerField(unique=True)
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
    excerpt_en = models.TextField()
    # original_af_tags contains the labels manually tagged by the taggers.
    # The structure is shown after the fields declaration below
    original_af_tags = models.JSONField(default=dict)
    export_data = models.JSONField(default=dict)
    af_exportable_data = models.JSONField(default=dict)
    extra = models.JSONField(default=dict)
    """
    NOTE:
    original_af_tags = {
        "sectors": ["xXx"],             # might not be present
        "subpillars_1d": ["xXx"],       # might not be present
        "subpillars_2d": ["xXx"],       # might not be present
    }
    """

    def __str__(self):
        return f"Original entry {self.original_entry_id}"


class ClassificationModel(BaseModel):
    name = models.CharField(max_length=200)
    version = models.CharField(max_length=20)
    model_uri = models.TextField(null=True, blank=True)
    defaults = models.JSONField(default=dict)

    class Meta:
        unique_together = ['name', 'version', 'model_uri']

    def __str__(self):
        return str(self.id)


class ClassificationPredictions(BaseModel):
    entry = models.OneToOneField(Entry, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    model = models.ForeignKey(ClassificationModel, on_delete=models.CASCADE)
    embeddings = ArrayField(models.FloatField(blank=True), blank=True, null=True)
    subpillars_1d = ArrayField(
        models.CharField(max_length=100, blank=True),
        blank=True,
        null=True
    )
    sectors = ArrayField(
        models.CharField(max_length=100, blank=True), blank=True, null=True
    )
    subpillars_2d = ArrayField(
        models.CharField(max_length=100, blank=True), blank=True, null=True
    )
    age = ArrayField(
        models.CharField(max_length=100, blank=True), blank=True, null=True
    )
    gender = ArrayField(
        models.CharField(max_length=100, blank=True), blank=True, null=True
    )
    affected_groups = ArrayField(
        models.CharField(max_length=100, blank=True), blank=True, null=True
    )
    specific_needs_groups = ArrayField(
        models.CharField(max_length=100, blank=True), blank=True, null=True
    )
    severity = ArrayField(
        models.CharField(max_length=100, blank=True), blank=True, null=True
    )

    def __str__(self):
        return str(self.entry.original_entry_id)


class ProjectWisePerfMetrics(models.Model):
    project_id = models.PositiveIntegerField()
    sectors_f1score = models.FloatField(blank=True, null=True)
    sectors_precision = models.FloatField(blank=True, null=True)
    sectors_recall = models.FloatField(blank=True, null=True)
    sectors_support = models.FloatField(blank=True, null=True)
    subpillars_1d_f1score = models.FloatField(blank=True, null=True)
    subpillars_1d_precision = models.FloatField(blank=True, null=True)
    subpillars_1d_recall = models.FloatField(blank=True, null=True)
    subpillars_1d_support = models.FloatField(blank=True, null=True)
    subpillars_2d_f1score = models.FloatField(blank=True, null=True)
    subpillars_2d_precision = models.FloatField(blank=True, null=True)
    subpillars_2d_recall = models.FloatField(blank=True, null=True)
    subpillars_2d_support = models.FloatField(blank=True, null=True)
    generated_at = models.DateTimeField()

    def __str__(self):
        return str(self.project_id)


class TagWisePerfMetrics(models.Model):
    tags = models.CharField(max_length=250, blank=True)
    precision = models.FloatField(blank=True, null=True)
    recall = models.FloatField(blank=True, null=True)
    f1score = models.FloatField(blank=True, null=True)
    support = models.IntegerField(blank=True, null=True)
    generated_at = models.DateTimeField()

    def __str__(self):
        return self.tags


class AllProjectPerfMetrics(models.Model):
    categories = models.CharField(max_length=250, blank=True)
    precision = models.FloatField(blank=True, null=True)
    recall = models.FloatField(blank=True, null=True)
    f1score = models.FloatField(blank=True, null=True)
    support = models.FloatField(blank=True, null=True)
    generated_at = models.DateTimeField()

    def __str__(self):
        return self.categories


class CategoryWiseMatchRatios(models.Model):
    sectors_completely_matched = models.FloatField(blank=True, null=True)
    sectors_missing = models.FloatField(blank=True, null=True)
    sectors_wrong = models.FloatField(blank=True, null=True)
    subpillars_1d_completely_matched = models.FloatField(blank=True, null=True)
    subpillars_1d_missing = models.FloatField(blank=True, null=True)
    subpillars_1d_wrong = models.FloatField(blank=True, null=True)
    subpillars_2d_completely_matched = models.FloatField(blank=True, null=True)
    subpillars_2d_missing = models.FloatField(blank=True, null=True)
    subpillars_2d_wrong = models.FloatField(blank=True, null=True)
    entry_id = models.PositiveIntegerField()
    project_id = models.PositiveIntegerField()
    generated_at = models.DateTimeField()

    def __str__(self):
        return str(self.entry_id)


class ProjectWiseMatchRatios(models.Model):
    project_id = models.PositiveIntegerField()
    sectors_completely_matched_mean = models.FloatField(blank=True, null=True)
    sectors_missing_mean = models.FloatField(blank=True, null=True)
    sectors_wrong_mean = models.FloatField(blank=True, null=True)
    subpillars_1d_completely_matched_mean = models.FloatField(blank=True, null=True)
    subpillars_1d_missing_mean = models.FloatField(blank=True, null=True)
    subpillars_1d_wrong_mean = models.FloatField(blank=True, null=True)
    subpillars_2d_completely_matched_mean = models.FloatField(blank=True, null=True)
    subpillars_2d_missing_mean = models.FloatField(blank=True, null=True)
    subpillars_2d_wrong_mean = models.FloatField(blank=True, null=True)
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

    def __str__(self):
        return str(self.reference_project_id)
