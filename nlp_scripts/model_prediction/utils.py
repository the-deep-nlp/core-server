from typing import Dict, Union

from .first_level_tags import FirstLevel
from .second_level_tags import SecondLevel
from .third_level_tags import ThirdLevel

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

def get_vf_list() -> Dict[str, Dict[str, Union[str, bool]]]:
    """
    Returns the NLP framework tags with their corresponding details
    """
    vf_tags_dict = {}

    first_lvl_tags = FirstLevel.first_level_lst()
    second_lvl_tags = SecondLevel.second_level_lst()
    third_lvl_tags = ThirdLevel.third_level_lst()

    def find_group(parent_id):
        if parent_id in vf_tags_dict:
            return vf_tags_dict[parent_id]["label"]
        return None

    for item in first_lvl_tags + second_lvl_tags + third_lvl_tags:
        vf_tags_dict[item["id"]] = {
            "label": item["key"],
            "group": item["key"] if not item["has_parent"] else find_group(item["parent_id"]),
            "is_category": not item["has_parent"],
            "parent_id": item["parent_id"]
        }
    return vf_tags_dict



