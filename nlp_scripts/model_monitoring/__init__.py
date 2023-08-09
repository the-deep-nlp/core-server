import pandas as pd

from core.models import Entry
from utils.transformations import batched


def create_entries_df(entries):
    df = pd.DataFrame()
    # TODO: create df
    return df


def entries_classification_tasks():
    entries_qs = Entry.objects.filter(classificationprediction__isnull=False)
    for entries_batch in batched(entries_qs, batch_size=500):
        pass
