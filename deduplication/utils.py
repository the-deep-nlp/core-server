from datasketch import MinHash, LeanMinHash

from utils.transformations import preprocess_text
from deduplication.models import LSHIndex


def get_minhash(txt: str):
    processed = preprocess_text(txt)
    items = set(processed.split())
    h = MinHash(num_perm=LSHIndex.NUM_PERM)
    for item in items:
        h.update(item.encode("utf8"))
    return LeanMinHash(h)


def insert_to_index(index, lead_id, lead_hash):
    try:
        index.insert(lead_id, lead_hash)
    except ValueError:
        pass


def get_similar_documents(lsh_index: LSHIndex, document: str):
    if lsh_index.index is None:
        return None
    dochash = get_minhash(document)
    return lsh_index.index.query(dochash)
