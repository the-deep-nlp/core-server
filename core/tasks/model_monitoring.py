from typing import List, Any
import datetime
from celery import shared_task
from django.db import transaction
import django
import django.utils.timezone as timezone
from django.conf import settings

import polars as pl

from utils.core import format_af_tags

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
from nlp_scripts.model_monitoring.utils import get_model_info
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
    model, created = ClassificationModel.objects.get_or_create(
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
    for row in dataframe.iter_rows():
        model_instance = model_class()
        for field in dataframe.columns:
            setattr(model_instance, field, getattr(row, field))
        model_instance.save()


def save_model_performance(df: pl.DataFrame):
    logger.info("Saving Model Performance")
    modelperf = ModelPerformance(df)
    df1 = modelperf.projectwise_perf_metrics()
    save_dataframe_to_model(df1, ProjectWisePerfMetrics)

    df2 = modelperf.per_tag_perf_metrics()
    save_dataframe_to_model(df2, TagWisePerfMetrics)

    df3 = modelperf.overall_projects_perf_metrics()
    save_dataframe_to_model(df3, AllProjectPerfMetrics)

    df4 = modelperf.calculate_ratios()
    save_dataframe_to_model(df4, CategoryWiseMatchRatios)

    df5 = modelperf.per_project_calc_ratios()
    save_dataframe_to_model(df5, ProjectWiseMatchRatios)
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
    feature_drift_df["entry_count"] = entry_len
    save_dataframe_to_model(feature_drift_df, ComputedFeatureDrift)
    logger.info("Saving Feature Drift Done")


@shared_task
def calculate_model_metrics():
    with transaction.atomic():
        yesterday = timezone.now() - datetime.timedelta(days=1)
        newly_added_entries: List[dict] = list(
            Entry.objects.filter(
                classificationpredictions__isnull=True,
                deep_entry_created_at__gte=yesterday,
                deep_entry_created_at__lt=timezone.now(),
            )
            .order_by("-id")
            .values(
                "original_entry_id",
                "excerpt_en",
                "original_af_tags",
                "lead__project__original_project_id",
            )[:1]
        )
        if not newly_added_entries:
            return

        # Create a data frame
        df = pl.DataFrame(newly_added_entries).rename(
            mapping={
                "original_entry_id": "entry_id",
                "excerpt_en": "excerpt",
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
        original_af_tags = df["original_af_tags"]

        sectors = [data.get("sectors", []) for data in original_af_tags]
        subpillar_1d = [data.get("subpillars_1d", []) for data in original_af_tags]
        subpillar_2d = [data.get("subpillars_2d", []) for data in original_af_tags]

        def _to_str_items(lst: List[List[Any]]):
            return [str(x) for x in lst]

        entry_df.with_columns(sectors=pl.Series("sectors", _to_str_items(sectors)))
        entry_df.with_columns(subpillars_1d=pl.Series("subpillars_1d", _to_str_items(subpillar_1d)))
        entry_df.with_columns(subpillars_2d=pl.Series("subpillars_2d", _to_str_items(subpillar_2d)))

        combined_df = output_df.join(entry_df, on="entry_id")
        current_df = combined_df[["project_id", "embeddings"]]

        # save model performance data
        create_model_performance.delay(combined_df.to_dicts())

        # save feature drift data
        create_feature_drift.delay(
            current_df.to_dicts(), len(newly_added_entries)
        )
