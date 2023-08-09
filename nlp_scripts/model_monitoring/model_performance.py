import logging
import datetime
import warnings
import json

from typing import List, Dict, Optional
from functools import partial

import polars as pl
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.metrics import precision_recall_fscore_support

from .utils import try_literal_eval

from .constants import (
    ROUNDOFF_DIGITS,
    CATEGORIES,
    SECTORS_LST,
    PILLARS_1D_LST,
    PILLARS_2D_LST,
    SUBPILLARS_1D_LST,
    SUBPILLARS_2D_LST,
    AGE_LST,
    DISPLACED_LST,
    GENDER_LST,
    NON_DISPLACED_LST,
    SEVERITY_LST,
    SPECIFIC_NEEDS_GROUPS_LST,
    SUBSECTORS_LST,
    AFFECTED_LST,
)

warnings.filterwarnings("ignore")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ModelPerformance:
    """
    Computes various model performance metrics
    """

    def __init__(self, dataframe: pl.DataFrame):
        """
        Categories: [
            "sectors",
            "pillars_1d",
            "pillars_2d",
            "subpillars_1d",
            "subpillars_2d",
            "age",
            "displaced",
            "gender",
            "non displaced",
            "severity",
            "specific_needs_groups"
        ]
        Input Dataframe: project_id, {category}
        """
        self.dataframe = dataframe
        self._preprocess_data()
        self._create_mlb_mappings()

    def _preprocess_data(self):
        """
        Preprocess the input dataframe basically converting serialized list to list
        """
        for category in CATEGORIES:
            if category in self.dataframe.columns:
                self.dataframe.with_columns(
                    pl.col(category)
                    .apply(try_literal_eval)
                    .cast(pl.List(pl.Utf8))
                    .alias(category)
                )
            category_pred = f"{category}_pred"
            if category_pred in self.dataframe.columns:
                self.dataframe.with_columns(
                    pl.col(category_pred)
                    .apply(try_literal_eval)
                    .cast(pl.List(pl.Utf8))
                    .alias(category_pred)
                )

    def _category_to_tags(self) -> dict:
        """
        Category to tags list mapping
        # Maintain this order respect to categories from utils.py
        """
        all_tags = [
            SECTORS_LST,
            PILLARS_1D_LST,
            PILLARS_2D_LST,
            SUBPILLARS_1D_LST,
            SUBPILLARS_2D_LST,
            AGE_LST,
            DISPLACED_LST,
            GENDER_LST,
            NON_DISPLACED_LST,
            SEVERITY_LST,
            SPECIFIC_NEEDS_GROUPS_LST,
            SUBSECTORS_LST,
            AFFECTED_LST
        ]
        return dict(zip(CATEGORIES, all_tags))

    def _create_mlb_mappings(self):
        """
        Create objects for multi-label encoding of all categories
        """
        self.mlb_sectors = MultiLabelBinarizer()
        self.mlb_sectors.fit_transform([[s] for s in SECTORS_LST])

        self.mlb_pillars_1d = MultiLabelBinarizer()
        self.mlb_pillars_1d.fit_transform([[s] for s in PILLARS_1D_LST])

        self.mlb_pillars_2d = MultiLabelBinarizer()
        self.mlb_pillars_2d.fit_transform([[s] for s in PILLARS_2D_LST])

        self.mlb_subpillars_1d = MultiLabelBinarizer()
        self.mlb_subpillars_1d.fit_transform([[s] for s in SUBPILLARS_1D_LST])

        self.mlb_subpillars_2d = MultiLabelBinarizer()
        self.mlb_subpillars_2d.fit_transform([[s] for s in SUBPILLARS_2D_LST])

        self.mlb_age = MultiLabelBinarizer()
        self.mlb_age.fit_transform([[s] for s in AGE_LST])

        self.mlb_displaced = MultiLabelBinarizer()
        self.mlb_displaced.fit_transform([[s] for s in DISPLACED_LST])

        self.mlb_gender = MultiLabelBinarizer()
        self.mlb_gender.fit_transform([[s] for s in GENDER_LST])

        self.mlb_non_displaced = MultiLabelBinarizer()
        self.mlb_non_displaced.fit_transform([[s] for s in NON_DISPLACED_LST])

        self.mlb_severity = MultiLabelBinarizer()
        self.mlb_severity.fit_transform([[s] for s in SEVERITY_LST])

        self.mlb_specific_needs_groups = MultiLabelBinarizer()
        self.mlb_specific_needs_groups.fit_transform(
            [[s] for s in SPECIFIC_NEEDS_GROUPS_LST]
        )

        self.mlb_subsectors = MultiLabelBinarizer()
        self.mlb_subsectors.fit_transform([[s] for s in SUBSECTORS_LST])

        self.mlb_affected = MultiLabelBinarizer()
        self.mlb_affected.fit_transform([[s] for s in AFFECTED_LST])

    def _category_to_mlb(self):
        """
        Mapping between the category and multi-label binarizer objects
        """
        return {
            "sectors": self.mlb_sectors,
            "pillars_1d": self.mlb_pillars_1d,
            "pillars_2d": self.mlb_pillars_2d,
            "subpillars_1d": self.mlb_subpillars_1d,
            "subpillars_2d": self.mlb_subpillars_2d,
            "age": self.mlb_age,
            "displaced": self.mlb_displaced,
            "gender": self.mlb_gender,
            "non_displaced": self.mlb_non_displaced,
            "severity": self.mlb_severity,
            "specific_needs_groups": self.mlb_specific_needs_groups,
            "subsectors": self.mlb_subsectors,
            "affected": self.mlb_affected
        }

    def label_transform(self):
        """
        Transforms the tags to numeric form using multi-label binarizer
        """
        cat_to_mlb = self._category_to_mlb()
        for category in CATEGORIES:
            if category in self.dataframe.columns:
                cat_name = f"{category}_transformed"
                self.dataframe = self.dataframe.with_columns(
                    pl.col(category)
                    .apply(lambda x: cat_to_mlb[category].transform([x])[0])
                    .alias(cat_name)
                )
            if f"{category}_pred" in self.dataframe.columns:
                cat_name = f"{category}_pred_transformed"
                cat_pred_name = f"{category}_pred"
                self.dataframe = self.dataframe.with_columns(
                    pl.col(cat_pred_name)
                    .apply(lambda x: cat_to_mlb[category].transform([x])[0])
                    .alias(cat_name)
                )

    def projectwise_perf_metrics(
        self, metrics_average_type: str = "macro"
    ) -> pl.DataFrame:
        """
        Calculates the project wise performance metrics
        Categories: [
            "sectors",
            "pillars_1d",
            "pillars_2d",
            "subpillars_1d",
            "subpillars_2d",
            "age",
            "displaced",
            "gender",
            "non displaced",
            "severity",
            "specific_needs_groups"
        ]
        Input Dataframe: project_id, {category}_transformed, {category}_pred_transformed
        Output Dataframe: project_id, {category}_precision, {category}_recall, {category}_f1score, generated_at
        """
        project_perf_metrics: dict = {}
        for category in CATEGORIES:
            if all(item in self.dataframe.columns for item in [f"{category}_transformed", f"{category}_pred_transformed"]):
                for project_grp in self.dataframe.groupby(
                    "project_id", maintain_order=True
                ):
                    # Note that
                    # project_grp[0] -> project_id
                    # project_grp[1] -> dataframe containing remaining data
                    precision, recall, f1score, _ = precision_recall_fscore_support(
                        y_true=project_grp[1][f"{category}_transformed"]
                        .apply(list)
                        .to_list(),
                        y_pred=project_grp[1][f"{category}_pred_transformed"]
                        .apply(list)
                        .to_list(),
                        average=metrics_average_type,
                        zero_division=0,
                    )
                    project_id = str(project_grp[0])
                    if project_id not in project_perf_metrics:
                        project_perf_metrics[project_id] = {
                            "project_id": project_id,
                            f"{category}_precision": np.round(precision, ROUNDOFF_DIGITS),
                            f"{category}_recall": np.round(recall, ROUNDOFF_DIGITS),
                            f"{category}_f1score": np.round(f1score, ROUNDOFF_DIGITS),
                            "generated_at": datetime.date.today(),
                        }
                    project_perf_metrics[project_id].update(
                        {
                            f"{category}_precision": np.round(precision, ROUNDOFF_DIGITS),
                            f"{category}_recall": np.round(recall, ROUNDOFF_DIGITS),
                            f"{category}_f1score": np.round(f1score, ROUNDOFF_DIGITS),
                        }
                    )
        return pl.DataFrame(list(project_perf_metrics.values()))

    def overall_projects_perf_metrics(
        self, metrics_average_type: str = "macro"
    ) -> pl.DataFrame:
        """
        Calculates the overall performance metrics irrespective of the projects
        Categories: [
            "sectors",
            "pillars_1d",
            "pillars_2d",
            "subpillars_1d",
            "subpillars_2d",
            "age",
            "displaced",
            "gender",
            "non displaced",
            "severity",
            "specific_needs_groups"
        ]
        Input Dataframe: {category}_transformed, {category}_pred_transformed
        Output Dataframe: category, precision, recall, f1score, generated_at
        category: List of group as mentioned above
        precision, recall, f1score: Evaluation performance metrics (0-1)
        generated_at: Date
        """
        all_projects_perf_metrics: dict = {}
        for category in CATEGORIES:
            if category in self.dataframe.columns:
                precision, recall, f1score, _ = precision_recall_fscore_support(
                    y_true=self.dataframe[f"{category}_transformed"]
                    .apply(list)
                    .to_list(),
                    y_pred=self.dataframe[f"{category}_pred_transformed"]
                    .apply(list)
                    .to_list(),
                    average=metrics_average_type,
                    zero_division=0,
                )
                all_projects_perf_metrics[category] = {
                    "category": category,
                    "precision": np.round(precision, ROUNDOFF_DIGITS),
                    "recall": np.round(recall, ROUNDOFF_DIGITS),
                    "f1score": np.round(f1score, ROUNDOFF_DIGITS),
                    "generated_at": datetime.date.today(),
                }
        if not all_projects_perf_metrics:
            return pl.DataFrame()
        return pl.DataFrame(list(all_projects_perf_metrics.values()))

    def per_tag_perf_metrics(self) -> Optional[pl.DataFrame]:
        """
        Calculates the performance metrics per tag
        Categories: [
            "sectors",
            "pillars_1d",
            "pillars_2d",
            "subpillars_1d",
            "subpillars_2d",
            "age",
            "displaced",
            "gender",
            "non displaced",
            "severity",
            "specific_needs_groups"
        ]
        Input Dataframe: {category}_transformed, {category}_pred_transformed
        Output Dataframe: tags, score, metric(type), generated_at
        tags refer to list of tags
        score refer to the score of the performance metric (0-1)
        metric refer to precision, recall or f1score
        generated_at refer to the date.
        """

        def generate_df_with_extra_cols(
            tags_scores_dict: dict, metrics_type: str
        ) -> Optional[pl.DataFrame]:
            if not tags_scores_dict:
                return None
            df_temp = pl.DataFrame(tags_scores_dict).transpose(
                include_header=True, header_name="tags", column_names=["score"]
            )
            return df_temp.with_columns(
                pl.lit(metrics_type).alias("metric"),
                pl.lit(datetime.date.today()).alias("generated_at"),
            )

        cat_to_tags: Dict[str, List[str]] = self._category_to_tags()

        tag_precision_perf_metrics: dict = {}
        tag_recall_perf_metrics: dict = {}
        tag_f1score_perf_metrics: dict = {}
        for category in CATEGORIES:
            if category in self.dataframe.columns:
                precision, recall, f1score, _ = precision_recall_fscore_support(
                    y_true=self.dataframe[f"{category}_transformed"]
                    .apply(list)
                    .to_list(),
                    y_pred=self.dataframe[f"{category}_pred_transformed"]
                    .apply(list)
                    .to_list(),
                    zero_division=0,
                )
                for tag, metricval in zip(cat_to_tags[category], precision):
                    tag_precision_perf_metrics[tag] = np.round(metricval, ROUNDOFF_DIGITS)
                for tag, metricval in zip(cat_to_tags[category], recall):
                    tag_recall_perf_metrics[tag] = np.round(metricval, ROUNDOFF_DIGITS)
                for tag, metricval in zip(cat_to_tags[category], f1score):
                    tag_f1score_perf_metrics[tag] = np.round(metricval, ROUNDOFF_DIGITS)

        precision_df = generate_df_with_extra_cols(tag_precision_perf_metrics, "precision")
        recall_df = generate_df_with_extra_cols(tag_recall_perf_metrics, "recall")
        f1score_df = generate_df_with_extra_cols(tag_f1score_perf_metrics, "f1score")

        if precision_df.is_empty() or recall_df.is_empty() or f1score_df.is_empty():
            return pl.DataFrame()
        return pl.concat([precision_df, recall_df, f1score_df], how="vertical")

    def _tags_matching_ratios(
        self, category, gt_embed: list, pred_embed: list
    ) -> dict:
        """
        Calculates the ratios based on the encoding values of the tags
        """
        completely_matched = [e1 == e2 for e1, e2 in zip(gt_embed, pred_embed)]
        missing = [e1 > e2 for e1, e2 in zip(gt_embed, pred_embed)]
        wrong = [e1 < e2 for e1, e2 in zip(gt_embed, pred_embed)]
        return {
            f"{category}_completely_matched": round(sum(completely_matched) / len(gt_embed), ROUNDOFF_DIGITS),
            f"{category}_missing": round(sum(missing) / len(gt_embed), ROUNDOFF_DIGITS),
            f"{category}_wrong": round(sum(wrong) / len(gt_embed), ROUNDOFF_DIGITS),
        }

    def calculate_ratios(self) -> pl.DataFrame:
        """
        Calculate the ratios of the categories
        Categories: [
            "sectors",
            "pillars_1d",
            "pillars_2d",
            "subpillars_1d",
            "subpillars_2d",
            "age",
            "displaced",
            "gender",
            "non displaced",
            "severity",
            "specific_needs_groups"
        ]
        Input Dataframe: project_id, {category}_transformed, {category}_pred_transformed
        Output Dataframe: project_id, completely_matched_{category}, missing_{category}, wrong_{category}, generated_at
        """
        final_df = pl.DataFrame()
        for category in CATEGORIES:
            if category in self.dataframe.columns:
                temp_lst = list(
                    map(
                        partial(self._tags_matching_ratios, category),
                        self.dataframe[f"{category}_transformed"].apply(list).to_list(),
                        self.dataframe[f"{category}_pred_transformed"].apply(list).to_list(),
                    )
                )
                if not temp_lst:
                    continue
                final_df = pl.concat(
                    [final_df, pl.DataFrame(temp_lst)], how="horizontal"
                )

        if len(final_df) == 0:
            return final_df
        return final_df.with_columns(
            self.dataframe["entry_id"].alias("entry_id"),
            self.dataframe["project_id"].alias("project_id"),
            pl.lit(datetime.date.today()).alias("generated_at"),
        )

    def per_project_calc_ratios(self) -> pl.DataFrame:
        """
        Calculates the per project ratio of the categories
        Categories: [
            "sectors",
            "pillars_1d",
            "pillars_2d",
            "subpillars_1d",
            "subpillars_2d",
            "age",
            "displaced",
            "gender",
            "non displaced",
            "severity",
            "specific_needs_groups"
        ]
        Input Dataframe: project_id, completely_matched_{category}, missing_{category}, wrong_{category},
        Output Dataframe: project_id, completely_matched_{category}_mean,\
        missing_{category}_mean, wrong_{category}_mean, generated_at
        """
        ratios_df = self.calculate_ratios()
        if ratios_df.is_empty():
            return ratios_df
        final_df = pl.DataFrame()
        for project_grp in ratios_df.groupby("project_id", maintain_order=True):
            temp_df = pl.DataFrame()
            project_id = project_grp[0]
            project_grp_df = project_grp[1]
            for category in CATEGORIES:
                if f"{category}_completely_matched" in project_grp_df.columns:
                    temp_df = temp_df.with_columns(
                        pl.lit(
                            np.round(project_grp_df[f"{category}_completely_matched"].mean(), ROUNDOFF_DIGITS)
                        ).alias(f"{category}_completely_matched_mean")
                    )
                if f"{category}_missing" in project_grp_df.columns:
                    temp_df = temp_df.with_columns(
                        pl.lit(np.round(project_grp_df[f"{category}_missing"].mean(), ROUNDOFF_DIGITS)).alias(
                            f"{category}_missing_mean"
                        )
                    )
                if f"{category}_wrong" in project_grp_df.columns:
                    temp_df = temp_df.with_columns(
                        pl.lit(np.round(project_grp_df[f"{category}_wrong"].mean(), ROUNDOFF_DIGITS)).alias(
                            f"{category}_wrong_mean"
                        )
                    )

            if len(temp_df) == 0:
                continue
            temp_df = temp_df.with_columns(
                pl.lit(project_id).alias("project_id"),
                pl.lit(datetime.date.today()).alias("generated_at"),
            )
            final_df = pl.concat([final_df, temp_df], how="vertical")
        return final_df


if __name__ == "__main__":
    # example dataframe
    pl_df = pl.DataFrame(
        {
            "project_id": [1111, 1234],
            "sectors": [
                json.dumps(
                    [
                        "first_level_tags->sectors->Agriculture",
                        "first_level_tags->sectors->Shelter",
                    ]
                ),
                json.dumps(["first_level_tags->sectors->Agriculture"]),
            ],
            "pillars_1d": [
                json.dumps(["first_level_tags->pillars_1d->Casualties"]),
                json.dumps(["first_level_tags->pillars_1d->Context"]),
            ],
            "sectors_pred": [
                json.dumps(
                    [
                        "first_level_tags->sectors->Agriculture",
                        "first_level_tags->sectors->Protection",
                    ]
                ),
                json.dumps(["first_level_tags->sectors->Agriculture"]),
            ],
            "pillars_1d_pred": [
                json.dumps(["first_level_tags->pillars_1d->Casualties"]),
                json.dumps(["first_level_tags->pillars_1d->Context"]),
            ],
        }
    )
    modelperf = ModelPerformance(dataframe=pl_df)
    modelperf.label_transform()
    print(modelperf.projectwise_perf_metrics())
