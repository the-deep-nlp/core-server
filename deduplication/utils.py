from datasketch import MinHash, LeanMinHash

from utils.transformations import preprocess_text
from core.models import Lead, Project
from deduplication.models import LSHIndex, LeadHash


def get_minhash(txt: str):
    processed = preprocess_text(txt)
    items = set(processed.split())
    h = MinHash(num_perm=LSHIndex.NUM_PERM)
    for item in items:
        h.update(item.encode('utf8'))
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


def create_lead_hash(
    dedup_request,
    lsh_index: LSHIndex
):
    """Creates lead hash object and corresponding lead/project as necessary"""
    project, _ = Project.objects.get_or_create(
        original_project_id=dedup_request.project_id,
        defaults={
            "location": "",
            "title": dedup_request.project_id,
        }
    )
    lead, _ = Lead.objects.get_or_create(
        original_lead_id=dedup_request.lead_id,
        defaults={
            "project": project,
            "text_extract": dedup_request.text_extract,
            "extraction_status": Lead.ExtractionStatus.SUCCESS,
            "confidentiality": Lead.Confidentiality.UNPROTECTED,
        }
    )
    # Create Lead hash
    lead_hash = get_minhash(dedup_request.text_extract)
    lead_hash_obj = LeadHash.objects.create(
        lead=lead,
        lsh_index=lsh_index,
        lead_hash=lead_hash,
    )
