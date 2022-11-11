from django.db import models

from core_server.base_models import BaseModel


class Organization(BaseModel):
    original_organization_id = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=50)
    long_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Project(BaseModel):
    original_project_id = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class AFMapping(BaseModel):
    af_name = models.CharField(max_length=200)
    original_af_id = models.PositiveIntegerField(unique=True)
    original_af_tags = models.JSONField(default=dict)
    nlp_tags = models.JSONField(default=dict)
    is_mapped_manually = models.BooleanField()

    def __str__(self):
        return self.af_name


class Lead(BaseModel):
    class Confidentiality(models.IntegerChoices):
        UNCLASSIFIED = 0, 'Unclassified'
        CLASSIFIED = 5, 'Classified'
        TOP_SECRET = 10, 'Top Secret'

    original_lead_id = models.PositiveIntegerField(unique=True)
    af_mapping = models.ForeignKey(AFMapping, on_delete=models.CASCADE)
    text_extract = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    authoring_org = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='authored_leads',
    )
    publishing_org = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='published_leads',
    )
    confidentiality = models.IntegerField(
        choices=Confidentiality.choices,
        default=Confidentiality.CLASSIFIED,
    )
    source_url = models.TextField()

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

    def __str__(self):
        return f'Original entry {self.original_entry_id}'


class ClassificationModel(BaseModel):
    name = models.CharField(max_length=200)
    version = models.CharField(max_length=20)
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
