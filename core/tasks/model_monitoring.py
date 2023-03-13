from celery import shared_task
import pandas as pd
from django.db import transaction
import django

from core.models import (
    Entry,
    Lead,
    Project,
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


def save_classification_prediction(df):
    classification_rows = df.to_dict("records")
    model_info = get_model_info("main-model-cpu")[0]
    model = ClassificationModel.objects.filter(
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

    # model_instances = [
    #     ClassificationPredictions(
    #         entry=Entry.objects.get(original_entry_id=int(record["entry_id"])),
    #         project=Project.objects.get(
    #             lead=Lead.objects.get(
    #                 entry=Entry.objects.get(original_entry_id=int(record["entry_id"]))
    #             )
    #         ),
    #         model=model,
    #         embeddings=record["embeddings"],
    #         subpillars_1d=record["subpillars_1d_pred"],
    #         sectors=record["sectors_pred"],
    #         subpillars_2d=record["subpillars_2d_pred"],
    #         age=record["age_pred"],
    #         gender=record["gender_pred"],
    #         affected_groups=record["affected_groups_pred"],
    #         specific_needs_groups=record["specific_needs_groups_pred"],
    #         severity=record["severity_pred"],
    #     )
    #     for record in df
    # ]

    predictions = ClassificationPredictions.objects.bulk_create(model_instances)
    return predictions


def save_dataframe_to_model(dataframe: pd.DataFrame, model_class: django.db.models.Model):
    for row in dataframe.itertuples(index=False):
        model_instance = model_class()
        for field in dataframe.columns:
            setattr(model_instance, field, getattr(row, field))
        model_instance.save()


def create_model_performance(df):
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


def set_project_id(row):
    project = Project.objects.get(
        lead=Lead.objects.get(
            entry=Entry.objects.get(original_entry_id=row["entry_id"])
        )
    )
    return project.original_project_id


@shared_task
def calculate_model_metrics():
    with transaction.atomic():
        newly_added_entries = list(
            Entry.objects.exclude(
                original_entry_id__in=ClassificationPredictions.objects.values_list(
                    "entry__original_entry_id", flat=True
                )
            )
            .order_by("-id")
            .values("original_entry_id", "excerpt_en", "original_af_tags")
        )
        # create a data frame
        df = pd.DataFrame(newly_added_entries).rename(
            columns={"original_entry_id": "entry_id", "excerpt_en": "excerpt"}
        )

        df["project_id"] = df.apply(set_project_id, axis=1)
        entry_df = df.drop(columns=["original_af_tags"])

        # generate output
        model_output = ClassificationModelOutput(
            entry_df,
            endpoint_name="main-model-cpu",
            aws_region="us-east-1",
            batch_size=1,
            prediction_required=True,
            embeddings_required=True,
        )
        output_df = model_output.generate_outputs()

        # save the generated output in a model
        save_classification_prediction(output_df)

        # prepare dataframe for model performance
        original_af_tags = df["original_af_tags"]
        entry_df["sectors"] = [data.get("sectors", []) for data in original_af_tags]
        entry_df["subpillars_1d"] = [
            data.get("subpillars_1d", []) for data in original_af_tags
        ]
        entry_df["subpillars_2d"] = [
            data.get("subpillars_2d", []) for data in original_af_tags
        ]
        combined_df = output_df.merge(entry_df, on="entry_id")
        create_model_performance(combined_df)
        current_df = combined_df[["project_id", "embeddings"]]

        # create feature drift
        reference_data_path = (
            ClassificationModel.objects.order_by("-id").first().train_data_uri
        )
        reference_data_df = pd.read_csv(reference_data_path)
        feature_drift = FeatureDrift(reference_data_df, current_df)
        feature_drift_df = feature_drift.compute_feature_drift(
            ref_n_samples=10, cur_n_samples=10
        )
        feature_drift_df['entry_count'] = len(newly_added_entries)
        save_dataframe_to_model(feature_drift_df, ComputedFeatureDrift)
