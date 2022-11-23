import pickle
from django.db import models

import logging

from core_server.base_models import BaseModel
from core.models import Lead, Project


logger = logging.getLogger(__name__)


class LSHIndex(BaseModel):
    """
    Uses datasketch LSH Index
    """
    THRESHOLD = 0.55
    NUM_PERM = 256

    class IndexStatus(models.TextChoices):
        CREATING = 'creating', 'Creating'
        CREATED = 'created', 'Created'

    name = models.CharField(max_length=256)
    status = models.CharField(
        max_length=20,
        choices=IndexStatus.choices,
        default=IndexStatus.CREATING,
    )
    project = models.OneToOneField(
        Project,
        null=True,
        on_delete=models.CASCADE,
        unique=True,
    )
    pickle_version = models.CharField(max_length=10, null=True)
    index_pickle = models.BinaryField(null=True)

    def load_index(self):
        """This sets the attribute index if pickle is present"""
        if hasattr(self, 'index_pickle') and self.index_pickle is not None \
                and self.pickle_version is not None:
            supported_formats = pickle.compatible_formats
            if self.pickle_version not in supported_formats:
                logger.warn('Pickle versions not compatible, setting index to None')  # noqa
                self._index = None
            else:
                self._index = pickle.loads(self.index_pickle)
        else:
            self._index = None
        self._index_loaded = True

    @property
    def index(self):
        if not self._index_loaded:
            self.load_index()
        return self._index

    @index.setter
    def index(self, value):
        self._index = value
        self.index_pickle = pickle.dumps(value)

    def __init__(self, *args, **kwargs):
        self._index_loaded = False
        super().__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        # Set self._index_loaded = False so that next time it is
        # accessed, it is reloaded
        self._index_loaded = False
        super().save(*args, **kwargs)


class LeadHash(BaseModel):
    """
    Object that stores hash of leads
    """
    lead = models.OneToOneField(Lead, on_delete=models.CASCADE)
    lsh_index = models.ForeignKey(LSHIndex, on_delete=models.CASCADE)

    lead_hash = models.BinaryField()

    class Meta:
        unique_together = ('lead', 'lsh_index')
