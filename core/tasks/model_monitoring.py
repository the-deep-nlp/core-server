from typing import List, Any, Optional
import datetime
from celery import shared_task
from django.db import transaction
import django
import django.utils.timezone as timezone
from django.conf import settings

import polars as pl

from core.models import (
    Entry,
    ClassificationPredictions,
    ClassificationModel,
    ProjectWisePerfMetrics,
    AllProjectPerfMetrics,
    CategoryWiseMatchRatios,
    ProjectWiseMatchRatios,
    TagWisePerfMetrics,
    ComputedFeatureDrift,
)
from core_server.settings import (
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    CLASSIFICATION_MODEL_ENDPOINT,
)
from nlp_scripts.model_monitoring.constants import CATEGORIES
from nlp_scripts.model_monitoring.utils import get_model_info, group_tags
from nlp_scripts.model_monitoring.generate_outputs import ClassificationModelOutput
from nlp_scripts.model_monitoring.model_performance import ModelPerformance
from nlp_scripts.model_monitoring.featuredrift import FeatureDrift

from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


def save_classification_prediction(df: pl.DataFrame):
    logger.info("Saving classification predictions")
    classification_rows = df.to_dicts()
    model_info = get_model_info(
        CLASSIFICATION_MODEL_ENDPOINT, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
    )[0]
    model, _ = ClassificationModel.objects.get_or_create(
        name=model_info["name"],
        version=model_info["version"],
        model_uri=model_info["model_uri"],
        defaults={
            "description": model_info["description"],
            "train_data_uri": model_info["reference_train_data"],
        },
    )
    entry_ids = [record["entry_id"] for record in classification_rows]
    entries = Entry.objects.filter(original_entry_id__in=entry_ids).prefetch_related(
        "lead", "lead__project"
    )

    records_dict = {record["entry_id"]: record for record in classification_rows}
    model_instances = [
        ClassificationPredictions(
            entry=entry,
            project=entry.lead.project,
            model=model,
            embeddings=records_dict[entry.original_entry_id]["embeddings"],
            subpillars_1d=records_dict[entry.original_entry_id]["subpillars_1d_pred"],
            sectors=records_dict[entry.original_entry_id]["sectors_pred"],
            subpillars_2d=records_dict[entry.original_entry_id]["subpillars_2d_pred"],
            age=records_dict[entry.original_entry_id]["age_pred"],
            gender=records_dict[entry.original_entry_id]["gender_pred"],
            affected_groups=records_dict[entry.original_entry_id][
                "affected_pred"
            ],
            specific_needs_groups=records_dict[entry.original_entry_id][
                "specific_needs_groups_pred"
            ],
            severity=records_dict[entry.original_entry_id]["severity_pred"],
        )
        for entry in entries
    ]

    predictions = ClassificationPredictions.objects.bulk_create(model_instances)
    logger.info("Saving classification predictions Done")
    return predictions


def save_dataframe_to_model(
    dataframe: pl.DataFrame, model_class: django.db.models.Model
):
    for row in dataframe.iter_rows(named=True):
        model_instance = model_class()
        for field in dataframe.columns:
            setattr(model_instance, field, row.get(field))
        model_instance.save()


def save_model_performance(df: pl.DataFrame):
    logger.info("Saving Model Performance")
    modelperf = ModelPerformance(df)
    modelperf.label_transform()
    df1 = modelperf.projectwise_perf_metrics()
    if not df1.is_empty():
        save_dataframe_to_model(df1, ProjectWisePerfMetrics)
    else:
        logger.info("Empty project wise performance data")

    df2 = modelperf.per_tag_perf_metrics()
    if not df2.is_empty():
        save_dataframe_to_model(df2, TagWisePerfMetrics)
    else:
        logger.info("Empty tag performance data")

    df3 = modelperf.overall_projects_perf_metrics()
    if not df3.is_empty():
        save_dataframe_to_model(df3, AllProjectPerfMetrics)
    else:
        logger.info("Empty project performance data")

    df4 = modelperf.calculate_ratios()
    if not df4.is_empty():
        save_dataframe_to_model(df4, CategoryWiseMatchRatios)
    else:
        logger.info("Empty ratio data")

    df5 = modelperf.per_project_calc_ratios()
    if not df5.is_empty():
        save_dataframe_to_model(df5, ProjectWiseMatchRatios)
    else:
        logger.info("Empty per project ratio data")

    logger.info("Saving Model Performance Done")


@shared_task
def create_model_performance(combined_data: List[dict]):
    save_model_performance(pl.from_dicts(combined_data))


@shared_task
def create_feature_drift(current_data: dict, entry_len: int):
    logger.info("Saving Feature Drift")
    current_df = pl.from_dict(current_data)
    reference_data_path = (
        ClassificationModel.objects.order_by("-id").first().train_data_uri
    )
    reference_data_df = pl.read_csv(reference_data_path)
    feature_drift = FeatureDrift(reference_data_df, current_df)
    feature_drift_df = feature_drift.compute_feature_drift(
        ref_n_samples=len(reference_data_df), cur_n_samples=len(current_df)
    )
    if feature_drift_df.is_empty():
        logger.warning("Feature drift output dataframe is empty.")
        return
    feature_drift_df = feature_drift_df.with_columns(entry_count=pl.lit(entry_len))
    save_dataframe_to_model(feature_drift_df, ComputedFeatureDrift)
    logger.info("Saving Feature Drift Done")


@shared_task
def calculate_model_metrics(is_daily_calculation=True, batch_size: Optional[int] = None):
    """
    This function is supposed to run on a daily basis. But sometimes, due to db
    reset or refetching/updating of all the entries, everything might be needed
    to calculate.
    """
    yesterday = timezone.now() - datetime.timedelta(days=1)
    entry_filter = {
        "deep_entry_created_at__gte": yesterday,
        "deep_entry_created_at__lt": timezone.now(),
    } if is_daily_calculation else {}
    with transaction.atomic():
        entries_qs = (
            Entry.objects.filter(
                classificationpredictions__isnull=True,
                **entry_filter
            )
            .order_by("-id")
            .values(
                "original_entry_id",
                "excerpt",
                "original_af_tags",
                "lead__project__original_project_id",
                "nlp_tags",
            )
        )
        newly_added_entries: list[dict] = list(entries_qs) if batch_size is None \
            else list(entries_qs[:batch_size])

        logger.info(f"Obtained {len(newly_added_entries)} entries to calculate model metrics")
        if not newly_added_entries:
            return

        # Create a data frame
        df = pl.DataFrame(newly_added_entries).rename(
            mapping={
                "original_entry_id": "entry_id",
                "lead__project__original_project_id": "project_id",
            }
        )

        # save into classification prediction
        entry_df = df.drop(columns=["original_af_tags"])
        model_output = ClassificationModelOutput(
            entry_df,
            region_name="us-east-1",
            batch_size=1,
            prediction_generation=True,
            embeddings_generation=True,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            endpoint_name=CLASSIFICATION_MODEL_ENDPOINT,
        )
        output_df = model_output.generate_outputs()
        save_classification_prediction(output_df)

        # prepare dataframe for model performance
        nlp_tags = df["nlp_tags"].to_list()
        nlp_tagss = [v["nlp_tags"] for v in nlp_tags]
        grouped_tags = group_tags(nlp_tagss)

        categories_data = {}
        for category in CATEGORIES:
            categories_data[category] = [data.get(category, []) for data in grouped_tags]

        def _to_str_items(lst: List[List[Any]]):
            return [str(x) for x in lst]

        for category in CATEGORIES:
            entry_df = entry_df.with_columns(x=pl.Series(f"{category}", categories_data[category]))
            entry_df = entry_df.rename({"x": category})

        combined_df = output_df.join(entry_df, on="entry_id")
        current_df = combined_df[["project_id", "embeddings"]]

        # save model performance data
        create_model_performance.delay(combined_df.to_dicts())

        # save feature drift data
        create_feature_drift.delay(current_df.to_dict(as_series=False), len(newly_added_entries))
