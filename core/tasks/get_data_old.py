"""
@main_author: Nicolo(nico@datafriendlyspace.org)
@modified_by: Bibek(bibek.pandey@togglecorp.com)
NOTE: this module is not in use at the moment. This exists just for reference.
"""

import pandas as pd

from utils.db import connect_db
from utils.decorators import log_time
from core.tasks import queries


def _clean_tags(tag):
    if tag is None:
        return ""
    elif type(tag) is int:
        return tag
    else:
        return (
            tag.lower()
            .replace("->->", "->")
            .replace("-> ", "->")
            .replace(" ->", "->")
            .replace("->none", "")
            .replace("->n/a", "")
            .replace("\t", "")
            .replace("•", "")
        )


def _flatten(t):
    return [item for sublist in t for item in sublist]


def _get_data(cursor, projects, query, query_type, final=True):
    total = []
    for proj in projects["id"].tolist():
        cursor.execute(query.format(proj))
        data = cursor.fetchall()
        data = pd.DataFrame(data, columns=[c.name for c in cursor.description])
        total.append(data)
    if final:
        data = None
        if query_type == "projects":
            data = pd.concat(total, axis=0).drop_duplicates(["id"])
        elif query_type in ["entries", "af_widget", "af_exportables"]:
            data = pd.concat(total, axis=0).drop_duplicates(
                ["id", "analysis_framework_id"]
            )
        elif query_type == "exportdata":
            data = pd.concat(total, axis=0).drop_duplicates(["id", "entry_id"])

        return data
    else:
        return total


@log_time()
def pull_data(cursor, prj_id):
    cursor.execute(
        """SELECT * FROM project_project WHERE id IN ({})""".format(
            str(prj_id).strip("(").strip(")")
        )
    )
    projects = cursor.fetchall()
    columns = [c.name for c in cursor.description]
    projects = pd.DataFrame(projects, columns=columns)

    with log_time("entries get_data"):
        entries = _get_data(cursor, projects, queries.entries_q, "entries")
    with log_time("af_widgets get_data"):
        af_widgets = _get_data(cursor, projects, queries.af_widget_q, "af_widget")
    with log_time("exportdata get_data"):
        exportdata = _get_data(cursor, projects, queries.exportdata_q, "exportdata")

    return (entries, af_widgets, exportdata)


def _fmt_nm(nm):
    return nm.replace(" ", "_").lower()


def master_dict(af_widgets):
    md = {}
    for v in af_widgets.iterrows():
        title = _fmt_nm(v[1]["title"])
        wtype = v[1]["widget_id"]

        if wtype == "matrix1dWidget":
            md[title + "_sub_pillars"] = []

        elif wtype == "matrix2dWidget":
            md[title + "_sectors"] = []
            md[title + "_sub_sectors"] = []
            md[title + "_sub_pillars"] = []

        else:
            md[title] = []

    return md


"""
About the _get_matrix_2d:
@author: Nicolo
I think that the way to manage this is to create only one time the master dict
and not each tile the main problem is to consider possible labels with same ids
across same kind widget; for example, if you consider multiple projects some
widget_key (and also specific ids of labels) can be same (element0,
element1...) Here you hardcoded "element1" but it's something we can
generalize, for example:
"""


def _get_id2label(frame):
    t = {}
    d = frame[frame.widget_id.isin(["matrix2dWidget"])]

    for c in d.iterrows():
        _, a = c
        prop = a.properties
        for p in prop.get("rows", []):
            t.update({p["key"]: p["label"]})
            for pp in p.get("subRows", []):
                t.update({pp["key"]: pp["label"]})
            for pp in p.get("cells", []):
                t.update({pp["key"]: pp["label"]})

        for p in prop.get("columns", []):
            t.update({p["key"]: p["label"]})
            for pp in p.get("subColumns", []):
                t.update({pp["key"]: pp["label"]})

        """
        idea: to avoid same key problem across different AFs,
        we can append the unique AF id in front of the key.

        about the structure of the dictionary:
        splitting between sectors, pillars... it's useless, we can create a plain structure.

        """
        # dict_.update({f"{a['analysis_framework_id']}_{a.key}": t})

    return t


def _reshape_report(a):
    a = a.split("-")
    real = []
    for i, c in enumerate(a):
        if c.isnumeric():
            real.append("-".join([a[i - 1], c]))
        else:
            real.append(c)

    for c in real:
        # removing noisy elements due to keys like sector-9, pillar-2 and so on...
        if any(c == x for x in ["sector", "pillar", "subpillar", "subsector"]):
            real.remove(c)

    return real


# omg = 0
def _get_values_one_row(ex, widget, id2label):
    """
    * iterate through individual tags and extract content
    * pulls all the widgets from the AF. note that 1d and 2d matrices have special handling
    *

    dict:
        for 2d widgets: add sectors: list, subpillars: list
        for 1d widgets: add subpillars: list
        for all other widgets: values : list
    """
    key_id = ex["common"]["widget_key"]
    title = widget[widget.key == key_id].title.tolist()
    return get_tags_data_for_exportable(ex, id2label, title)


def get_tags_data_for_exportable(
    ex,
    id2label,
    title=None
):
    key_title = "MISSING"

    if "common" in ex.keys():
        common = ex["common"]
        if len(common) > 0 and "widget_id" in common:
            tip = common["widget_id"]
            if "widget_key" in common:
                if title:
                    key_title = _fmt_nm(title[0])
        else:
            tip = "empty"
    else:
        excel = ex["excel"]
        if type(excel) is dict:
            keys = excel.keys()
            if "value" in keys:
                tip = "no_common_multiselectWidget"
            elif "values" in keys and "report" in ex.keys():
                tip = "no_common_matrix2dWidget"
            elif "values" in keys and "report" not in ex.keys():
                tip = "raw"
            else:
                print("empty tip in no common for project, value is", ex)
                tip = "empty"
        else:
            tip = "empty"

    if tip in ["geoWidget", "dateRangeWidget"]:
        output = ex["common"]["values"]

    elif tip in [
        "dateWidget",
        "multiselectWidget",
        "selectWidget",
        "timeWidget",
    ]:
        output = ex["common"]["value"]

    elif tip in [
        "numberWidget",
        "scaleWidget",
        "textWidget",
        "no_common_multiselectWidget",
    ]:
        output = ex["excel"]["value"]

    elif tip == "organigramWidget":
        """
        must be careful here, the organigram it's a (for unknown reason) a list of list
        sometimes with empty strings values also

        better to use something like:
        master[key_title] = [a for e in c["excel")["values") for a in e if a]

        """
        output = [c for a in ex["excel"]["values"] for c in a if c]

    elif tip == "matrix1dWidget":
        rep = ex["excel"]["values"]
        sub_pillars = []

        for r in rep:
            sub_pillars.append(f"{r[0]}->{r[1]}")

        output = sub_pillars

    elif tip in ["matrix2dWidget", "no_common_matrix2dWidget"]:
        sectors, sub_sectors, sub_pillars = [], [], []
        rep = ex["report"]["keys"]

        m2widget = id2label  # [key)

        for r in rep:
            keys = _reshape_report(r)

            if len(keys) == 3:
                # if there is no subsector tag
                sect = m2widget.get(keys[0])
                pill = m2widget.get(keys[1])
                sub_pill = m2widget.get(keys[2])

                sectors.append(sect)
                sub_pillars.append(f"{pill}->{sub_pill}")

            elif len(keys) == 4:
                # if there's a subsector
                sect = m2widget.get(keys[0])
                sub_sect = m2widget.get(keys[1])
                pill = m2widget.get(keys[2])
                sub_pill = m2widget.get(keys[3])

                sectors.append(sect)
                sub_sectors.append(f"{sect}->{sub_sect}")
                sub_pillars.append(f"{pill}->{sub_pill}")

        output = sectors + sub_sectors + sub_pillars
        """
        it's not correct at this point -translating widget tags into raw tags- to infer these keys.
        The reason is that (probably except only for the sectors) our mapping sometimes doesn't reflect
        the widgets "classification" (especially in less common AFs).
        For example a matrix2dwidget tag in one AF can be considered as a (sub)pillar-1d in the NLP AF.
        """

    elif key_title == "MISSING":
        output = ["MISSING"]

    elif tip == "empty":
        output = []

    elif tip == "raw":
        output = ex["excel"]["values"]

    else:
        raise Exception("widget not found!")

    if output is None:
        # print("project_id", proj_id_tmp, "not list in", tip, ", value is:", c)
        output = []

    if type(output) is not list:
        output = [output.strip()] if type(output) is str else [output]

    # some cleaning
    if len(output) > 0:
        output = _flatten(output) if type(output[0]) is list else output
        output = [_clean_tags(one_output) for one_output in output]
        output = [
            one_output
            for one_output in output
            if one_output not in ["nan", "none", "", "n/a"]
        ]

        # output dict if value is not emtpy and empty list if value is empty
        output = {tip: output}
    else:
        output = []

    """
    Proposal: keeping "tip" (the widget type name) always as keys of the output also
    for primary tags
    """

    return output


def get_values(exports, widgets):
    id2label = _get_id2label(widgets)

    values = []
    for ex in exports.data:
        try:
            output_tmp = _get_values_one_row(ex, widgets, id2label)
        except Exception as e:
            print("error:", e, "in project_id:", proj_id_tmp)
            output_tmp = {"outputs": "error"}

        values.append(output_tmp)

    return values


def merge_dicts(x):
    return {k: v for d in x.dropna() for k, v in d.items()}


@log_time()
def fetch_data(prj_id):
    global proj_id_tmp

    proj_id_tmp = prj_id
    cursor = connect_db()

    entries, af_widgets, exportdata = pull_data(cursor, prj_id)
    values = get_values(exportdata, af_widgets)
    # print(values)

    total = pd.concat([exportdata, pd.DataFrame(values)], axis=1)
    # return total

    # keep only dicts (empty fields returned as lists)
    total = total[total["outputs"].apply(lambda x: type(x) is dict)]

    entries_labeled = pd.merge(
        entries,
        total,
        how="inner",
        left_on="id",
        right_on="entry_id",
        suffixes=("_entry", "_exportdata"),
    )

    entries_labeled = entries_labeled[entries_labeled.entry_type == "excerpt"]

    en = entries_labeled[["id_entry", "outputs"]].groupby("id_entry").agg(merge_dicts)
    en.reset_index(inplace=True)

    entries_ = entries[
        [
            "id",
            "created_at",
            "modified_at",
            "excerpt",
            "entry_type",
            "analysis_framework_id",
            # "created_by_id",
            "lead_id",
            # "modified_by_id",
            "project_id",
            "title",
        ]
    ].drop_duplicates()

    entries_ = entries_[entries_.excerpt.notna()]
    # print("pull leads")
    raw = (
        pd.merge(entries_, en, right_on="id_entry", left_on="id", how="inner")
        .rename(columns={"id": "entry_id"})
        .drop(columns=["id_entry"])
    )
    """cursor.execute(queries.lead_q)
    leads_raw = pd.DataFrame(
        cursor.fetchall(), columns=[c.name for c in cursor.description]
    )
    leads_raw = leads_raw[
        [
            "id",
            "title",
            "source_id",
            "author_id",
            "confidentiality",
            #"text",
            "url",
            #"status",
            "published_on",
            "source_type",
        ]
    ]
    raw = pd.merge(
        raw,
        leads_raw,
        left_on="lead_id",
        right_on="id",
        how="left",
        suffixes=("", "_lead"),
    )"""

    cursor.close()
    cursor.connection.close()
    return raw


if __name__ == "__main__":
    fetch_data(3019)
