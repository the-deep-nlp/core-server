from django.db import models

from core_server.base_models import BaseModel
from core.models import Lead, Project


class EncodingType(models.TextChoices):
    GLOVE_6B_300 = 'glove_6b_300', 'Glove 6B 300d'
    GLOVE_840B_300 = 'glove_840b_300', 'Glove 840B 300d'
    LSH_256_PERMS = 'lsh_256_perms', 'LSH 256 Perms'
    LSH_128_PERMS = 'lsh_128_perms', 'LSH 128 Perms'


class LSHIndex(BaseModel):
    name = models.CharField(max_length=256)
    project = models.ForeignKey(Project, null=True, on_delete=models.CASCADE)
    index_url = models.TextField()
    encoding_type = models.CharField(
        max_length=50,
        choices=EncodingType.choices
    )


class LeadVectorsNLP(BaseModel):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    lsh_index = models.ForeignKey(LSHIndex, on_delete=models.CASCADE)
    encoding_type = models.CharField(
        max_length=50,
        choices=EncodingType.choices
    )
    encoding = models.JSONField()

    def save(self, *args, **kwargs):
        if self.encoding_type != self.lsh_index.encoding_type:
            raise Exception('Encoding types of index and lead differ')
        super().save(*args, **kwargs)
