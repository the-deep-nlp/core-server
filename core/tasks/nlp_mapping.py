"""
@main_author: Selim(selim@datafriendlyspace.org)
@modified_by: Nico(nico@datafriendlyspace.org)
"""

import os
import re
import pandas as pd
from ast import literal_eval
from typing import Dict, Optional
from collections import defaultdict

from core.tasks import queries
from utils.db import connect_db, CursorWrapper


DEFAULT_MAPPING_PATH = os.path.join(
    os.path.dirname(__file__),
    "tags_mapping_sheet.csv"
)


mapping_widgets = [
    "matrix2dWidget",
    "multiselectWidget",
    "no_common_matrix2dWidget",
    "organigramWidget",
    "selectWidget",
    "raw",
    "scaleWidget",
    "no_common_multiselectWidget",
    "matrix1dWidget",
]

original_levels_cols = [
    "Original first level",
    "Original second level",
    "Original third level",
]
date_regex = re.compile(r"\d\d-\d\d-\d\d\d\d")


def _custom_eval(x):
    if str(x) == "nan":
        return {}
    if str(x) == "[None]":
        return {}
    if type(x) is list:
        return x
    if type(x) is dict:
        return x
    else:
        return literal_eval(x)


def get_mapping_sheet(path: Optional[str] = None):

    mapping_sheet = pd.read_csv(path or DEFAULT_MAPPING_PATH)
    mapping_sheet["mapped_nlp"] = mapping_sheet["mapped_nlp"].apply(_custom_eval)

    return mapping_sheet


def get_geolocation_dict(cursor: Optional[CursorWrapper] = None):

    if not cursor:
        cursor = connect_db()

    cursor.execute(queries.geolocation_q)
    data = cursor.fetchall()
    data = pd.DataFrame(data, columns=[c.name for c in cursor.description])
    geo_locations_dict = dict(
        zip(data["id"].tolist(), data["title"].tolist())
    )
    return geo_locations_dict


def get_nlp_outputs(
    data: dict,
    hum_mapping_sheet: pd.DataFrame,
    geo_locations_dict: Dict[int, str],
):
    mapping_dict = defaultdict(
        list
    )
    too_many_rows, no_mapping = set(), set()
    nlp_one_output = defaultdict(list)

    # dates
    dates_tmp = []
    for one_date_widget_type in ["dateRangeWidget", "dateWidget"]:
        if one_date_widget_type in data:
            dates_tmp.extend(
                [
                    one_date
                    for one_date in data[one_date_widget_type]
                    if one_date is not None
                ]
            )

    # geo_locations
    if "geoWidget" in data:
        geo_location_output = [
            geo_locations_dict.get(one_loc_id)
            for one_loc_id in data["geoWidget"]
        ]
    else:
        geo_location_output = []

    # nlp mapping widgets
    for one_widget_type in mapping_widgets:
        if one_widget_type in data:
            outputs_one_widget = data[one_widget_type]

            for item in outputs_one_widget:
                if not str(item) in ["nan", "none", "", "n/a"]:
                    if item.isdigit():
                        geo_location_output.append(
                            geo_locations_dict.get(int(item))
                        )

                    elif date_regex.match(item):
                        dates_tmp.append(item)

                    else:
                        all_items = item.strip().split("->")

                        last_item = all_items[-1]

                        if item not in mapping_dict:
                            if len(all_items) == 1:
                                # secondary tags or isolated items
                                mapping_row = hum_mapping_sheet[
                                    hum_mapping_sheet.apply(
                                        lambda x: any(
                                            [
                                                last_item == x[one_level_original]
                                                for one_level_original in original_levels_cols
                                            ]
                                        ),
                                        axis=1,
                                    )
                                ].copy()
                            # subpillars, subsectors
                            else:  # len(all_items) == 2:
                                second_last_item = all_items[-2]
                                mapping_row = hum_mapping_sheet[
                                    hum_mapping_sheet.apply(
                                        lambda x: second_last_item
                                        == x["Original first level"]
                                        and last_item == x["Original second level"],
                                        axis=1,
                                    )
                                ].copy()

                            if len(mapping_row) == 1:
                                one_mapped_item = mapping_row.iloc[0]["mapped_nlp"]

                                nlp_one_output["nlp_tags"].extend(one_mapped_item)
                                mapping_dict[item] = one_mapped_item

                            elif len(mapping_row) > 1:
                                all_mapped_nlp = (
                                    mapping_row["mapped_nlp"].apply(str).tolist()
                                )
                                if len(set(all_mapped_nlp)) == 1:
                                    one_mapped_item = mapping_row.iloc[0][
                                        "mapped_nlp"
                                    ]

                                    nlp_one_output["nlp_tags"].extend(
                                        one_mapped_item
                                    )
                                    mapping_dict[item] = one_mapped_item
                                else:
                                    first_level_mapped_row = hum_mapping_sheet[
                                        hum_mapping_sheet.apply(
                                            lambda x: x["Original first level"]
                                            == last_item
                                            and str(x["Original second level"])
                                            == "nan",
                                            axis=1,
                                        )
                                    ].copy()

                                    if len(first_level_mapped_row) == 1:
                                        one_mapped_item = (
                                            first_level_mapped_row.iloc[0][
                                                "mapped_nlp"
                                            ]
                                        )

                                        nlp_one_output["nlp_tags"].extend(
                                            one_mapped_item
                                        )
                                        mapping_dict[item] = one_mapped_item
                                    else:
                                        too_many_rows.add(item)
                                        mapping_dict[item] = "too_many_rows"
                            else:
                                no_mapping.add(item)
                                mapping_dict[item] = "no_mapping"

                        elif mapping_dict[item] not in [
                            "no_mapping",
                            "too_many_rows",
                        ]:
                            nlp_one_output["nlp_tags"].extend(mapping_dict[item])

    nlp_one_output["geo_location"] = [
        one_loc for one_loc in geo_location_output if one_loc is not None
    ]

    if len(dates_tmp) > 0:
        dates_output = dates_tmp[0]
    else:
        dates_output = "-"

    nlp_one_output["excerpt_date"] = dates_output
    nlp_one_output["nlp_tags"] = list(set(nlp_one_output["nlp_tags"]))

    return nlp_one_output, mapping_dict
