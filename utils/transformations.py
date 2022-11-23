import re
from datasketch import LeanMinHash


def batched(iterable, batch_size=100):
    batches = []
    for i, x in enumerate(iterable):
        batches.append(x)
        if (i+1) % batch_size == 0:
            yield batches
            batches = []
    if batches:
        yield batches
    return


def preprocess_text(txt: str):
    # Remove punctuations and lowercase
    lower = ' '.join(txt.split()).lower()
    return re.sub(r'[^a-z ]', '', lower)


def serialize_minhash(minhash: LeanMinHash):
    buf = bytearray(minhash.bytesize())
    minhash.serialize(buf)
    return buf
