import datetime
from celery import shared_task
import pandas as pd
from django.db import transaction
import django
import django.utils.timezone as timezone
from django.conf import settings

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
from nlp_scripts.model_monitoring.utils import get_model_info
from nlp_scripts.model_monitoring.generate_outputs import ClassificationModelOutput
from nlp_scripts.model_monitoring.model_performance import ModelPerformance
from nlp_scripts.model_monitoring.featuredrift import FeatureDrift

from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


def save_classification_prediction(df):
    logger.info("Saving classification predictions")
    classification_rows = df.to_dict("records")
    model_info = get_model_info("main-model-cpu")[0]
    model, created = ClassificationModel.objects.get_or_create(
        name=model_info["name"],
        version=model_info["version"],
        model_uri=model_info["model_uri"],
        defaults={
            "description": model_info["description"],
            "train_data_uri": model_info["reference_train_data"]
        }
    )
    entry_ids = [record['entry_id'] for record in classification_rows]
    entries = Entry.objects.filter(
        original_entry_id__in=entry_ids
    ).prefetch_related('lead', 'lead__project')

    records_dict = {
        record["entry_id"]: record
        for record in classification_rows
    }
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
            affected_groups=records_dict[entry.original_entry_id]["affected_groups_pred"],
            specific_needs_groups=records_dict[entry.original_entry_id]["specific_needs_groups_pred"],
            severity=records_dict[entry.original_entry_id]["severity_pred"],
        )
        for entry in entries
    ]

    predictions = ClassificationPredictions.objects.bulk_create(model_instances)
    logger.info("Saving classification predictions Done")
    return predictions


def save_dataframe_to_model(dataframe: pd.DataFrame, model_class: django.db.models.Model):
    for row in dataframe.itertuples(index=False):
        model_instance = model_class()
        for field in dataframe.columns:
            setattr(model_instance, field, getattr(row, field))
        model_instance.save()


def save_model_performance(df):
    logger.info("Saving Model Performance")
    modelperf = ModelPerformance(df)
    df1 = modelperf.project_wise_perf_metrics()
    save_dataframe_to_model(df1, ProjectWisePerfMetrics)

    df2 = modelperf.per_tag_perf_metrics()
    save_dataframe_to_model(df2, TagWisePerfMetrics)

    df3 = modelperf.all_projects_perf_metrics()
    save_dataframe_to_model(df3, AllProjectPerfMetrics)

    df4 = modelperf.calculate_ratios()
    save_dataframe_to_model(df4, CategoryWiseMatchRatios)

    df5 = modelperf.per_project_calc_ratios()
    save_dataframe_to_model(df5, ProjectWiseMatchRatios)
    logger.info("Saving Model Performance Done")


def set_project_id(row, dict):
    return dict[row["entry_id"]]


@shared_task
def create_model_performance(combined_df):
    save_model_performance(pd.DataFrame.from_dict(combined_df))


@shared_task
def create_feature_drift(current_df, entry_len):
    logger.info("Saving Feature Drift")
    current_df = pd.DataFrame.from_dict(current_df)
    reference_data_path = (
        ClassificationModel.objects.order_by("-id").first().train_data_uri
    )
    reference_data_df = pd.read_csv(reference_data_path)
    feature_drift = FeatureDrift(reference_data_df, current_df)
    feature_drift_df = feature_drift.compute_feature_drift(
        ref_n_samples=len(reference_data_df), cur_n_samples=len(current_df)
    )
    feature_drift_df['entry_count'] = entry_len
    save_dataframe_to_model(feature_drift_df, ComputedFeatureDrift)
    logger.info("Saving Feature Drift Done")


@shared_task
def calculate_model_metrics():
    with transaction.atomic():
        yesterday = timezone.now() - datetime.timedelta(days=1)
        newly_added_entries = list(
            Entry.objects.filter(
                classificationpredictions__isnull=True,
                deep_entry_created_at__gte=yesterday,
                deep_entry_created_at__lt=timezone.now()
            )
            .order_by("-id")
            .values("original_entry_id", "excerpt_en", "original_af_tags", "lead__project__original_project_id")
        )
        if not newly_added_entries:
            return
        # create a data frame
        df = pd.DataFrame(newly_added_entries).rename(
            columns={"original_entry_id": "entry_id", "excerpt_en": "excerpt"}
        )

        # save project id
        entry_project_id_dict = {
            entry["original_entry_id"]: entry["lead__project__original_project_id"]
            for entry in newly_added_entries
        }
        df["project_id"] = df.apply(set_project_id, axis=1, args=(entry_project_id_dict,))

        # save into classification prediction
        entry_df = df.drop(columns=["original_af_tags"])
        model_output = ClassificationModelOutput(
            entry_df,
            endpoint_name="main-model-cpu",
            aws_region="us-east-1",
            batch_size=1,
            prediction_required=True,
            embeddings_required=True,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
        )
        output_df = model_output.generate_outputs()
        save_classification_prediction(output_df)

        # prepare dataframe for model performance
        original_af_tags = df["original_af_tags"]

        sectors = [data.get("sectors", []) for data in original_af_tags]
        subpillar_1d = [data.get("subpillars_1d", []) for data in original_af_tags]
        subpillar_2d = [data.get("subpillars_2d", []) for data in original_af_tags]

        entry_df["sectors"] = pd.Series(format_af_tags(sectors))
        entry_df["subpillars_1d"] = pd.Series(format_af_tags(subpillar_1d))
        entry_df["subpillars_2d"] = pd.Series(format_af_tags(subpillar_2d))

        combined_df = output_df.merge(entry_df, on="entry_id")
        current_df = combined_df[["project_id", "embeddings"]]

        # save model performance data
        create_model_performance.delay(combined_df.to_dict("records"))

        # save feature drift data
        create_feature_drift.delay(current_df.to_dict("records"), len(newly_added_entries))
