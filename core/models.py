from django.db import models

from core_server.base_models import BaseModel


class DeepDataFetchTracker(BaseModel):
    last_fetched_org_created_at = models.DateTimeField(null=True)
    last_fetched_af_created_at = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        if self.pk is None and DeepDataFetchTracker.objects.first() is not None:
            raise Exception('Cannot create multiple trackers')
        super().save(*args, **kwargs)


class ToFetchProject(BaseModel):
    """This model keeps track of the projects whose data needs to be fetched.
    Also keeps track of last leads and entries fetched
    """
    class FetchStatus(models.TextChoices):
        NOT_FETCHED = 'not_fetched', 'Not Fetched'
        FETCHED = 'fetched', 'Fetched'
        ERRORED = 'errored', 'Errored'
        NOT_FOUND = 'not_found', 'Not Found'

    original_project_id = models.PositiveIntegerField(unique=True)
    status = models.CharField(
        max_length=20,
        choices=FetchStatus.choices,
        default=FetchStatus.NOT_FETCHED,
    )
    last_fetched_lead_created_at = models.DateTimeField(null=True, blank=True)
    last_fetched_entry_created_at = models.DateTimeField(null=True, blank=True)
    error = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.original_project_id)


class Organization(BaseModel):
    original_organization_id = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=50)
    long_name = models.CharField(max_length=50)
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
    af_mapping = models.ForeignKey(
        AFMapping,
        null=True,
        on_delete=models.CASCADE
    )
    to_fetch_project = models.ForeignKey(
        ToFetchProject,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    extra = models.JSONField(default=dict)

    def __str__(self):
        return self.title


class Lead(BaseModel):
    class Confidentiality(models.TextChoices):
        UNPROTECTED = 'unprotected', 'Public'
        RESTRICTED = 'restricted', 'Restricted'
        CONFIDENTIAL = 'confidential', 'Confidential'

    class ExtractionStatus(models.IntegerChoices):
        PENDING = 0, 'Pending'
        STARTED = 1, 'Started'
        RETRYING = 4, 'Retrying'
        SUCCESS = 2, 'Success'
        FAILED = 3, 'Failed'

    original_lead_id = models.PositiveIntegerField(unique=True)
    title = models.CharField(max_length=255)
    extraction_status = models.SmallIntegerField(
        choices=ExtractionStatus.choices, default=ExtractionStatus.PENDING
    )
    text_extract = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    authoring_org = models.ForeignKey(
        Organization,
        null=True,
        on_delete=models.CASCADE,
        related_name='authored_leads',
    )
    publishing_org = models.ForeignKey(
        Organization,
        null=True,
        on_delete=models.CASCADE,
        related_name='published_leads',
    )
    confidentiality = models.CharField(
        max_length=30,
        choices=Confidentiality.choices,
        default=Confidentiality.UNPROTECTED
    )
    source_url = models.TextField()
    extra = models.JSONField(default=dict)

    def __str__(self):
        return self.text_extract[:50]


class Entry(BaseModel):
    original_entry_id = models.PositiveIntegerField(unique=True)
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    original_lang = models.CharField(max_length=50)
    excerpt_en = models.TextField()
    excerpt_es = models.TextField()
    excerpt_fr = models.TextField()
    excerpt_pt = models.TextField()
    original_af_tags = models.JSONField(default=dict)
    nlp_af_tags = models.JSONField(default=dict)
    export_data = models.JSONField(default=dict)
    af_exportable_data = models.JSONField(default=dict)
    extra = models.JSONField(default=dict)

    def __str__(self):
        return f'Original entry {self.original_entry_id}'


class ClassificationModel(BaseModel):
    name = models.CharField(max_length=200)
    version = models.CharField(max_length=20)
    url = models.TextField(null=True, blank=True)
    description = models.TextField()
    extra_info = models.JSONField(default=dict)

    def __str__(self):
        return self.name


class ClassificationPredictions(BaseModel):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    model = models.ForeignKey(ClassificationModel, on_delete=models.CASCADE)
    original_en_predictions = models.JSONField(default=dict)
    original_es_predictions = models.JSONField(default=dict)
    original_fr_predictions = models.JSONField(default=dict)
    original_pt_predictions = models.JSONField(default=dict)
    nlp_en_predictions = models.JSONField(default=dict)
    nlp_es_predictions = models.JSONField(default=dict)
    nlp_fr_predictions = models.JSONField(default=dict)
    nlp_pt_predictions = models.JSONField(default=dict)

    def __str__(self):
        return self.entry


class LeadVectorsNLP(BaseModel):
    class EncodingType(models.TextChoices):
        GLOVE_6B_300 = 'glove_6b_300', 'Glove 6B 300d'
        GLOVE_840B_300 = 'glove_840b_300', 'Glove 840B 300d'
        LSH_256_PERMS = 'lsh_256_perms', 'LSH 256 Perms'
        LSH_128_PERMS = 'lsh_128_perms', 'LSH 128 Perms'

    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    encoding_type = models.CharField(
        max_length=50,
        choices=EncodingType.choices
    )
    encoding = models.JSONField()
