from typing import Dict


def find_tag_path(total_tags, tagid, idx=0):
    """
    Generates the Tags path
    """
    for tag in total_tags[idx]:
        if tag["id"] == tagid and tag["has_parent"]:
            return find_tag_path(total_tags, tag["parent_id"], idx=idx + 1) + [tagid]
    return [tagid]


def get_tag_ids(total_tags, taglist, idx=0):
    """
    Retrieves the tag IDs
    """
    for tag in total_tags[idx]:
        if tag["key"] == taglist[idx]:
            if idx >= len(total_tags) - 1:
                return [tag.get("id", None)]
            else:
                return [tag.get("id", None)] + get_tag_ids(
                    total_tags, taglist, idx=idx + 1
                )
    return [None]


def get_vf_list(total_tags, vf_tags: Dict = {}, idx=0):
    """
    Retrieves the NLP framework list
    """
    if idx >= len(total_tags):
        return vf_tags
    for tag in total_tags[idx]:
        vf_tags[tag["id"]] = {"label": tag["key"], "parent_id": tag["parent_id"]}
    return get_vf_list(vf_tags, idx=idx + 1)
