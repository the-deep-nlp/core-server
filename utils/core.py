import re


def format_af_tags(tags):
    tags_list = []
    for tag in tags:
        tag_list = []
        for t in tag:
            tag_list.append(re.sub(r"\s*->\s*", "->", t.split("->", 1)[1]))
        tags_list.append(tag_list)
    return tags_list
