from celery import shared_task
import pandas as pd
from django.db import transaction

from core.models import (
    Entry,
    Lead,
    Project,
    ClassificationPredictions,
    ClassificationModel,
    ProjectWisePerfMatrices,
    AllProjectPerfMatrics,
    CategoryWiseMatchRatios,
    ProjectWiseMatchRatios,
    TagWisePerfMatrics,
    ComputedFeatureDrift,
)
from nlp_scripts.model_monitoring.utils import get_model_info
from nlp_scripts.model_monitoring.generate_outputs import ClassificationModelOutput
from nlp_scripts.model_monitoring.model_performance import ModelPerformance
from nlp_scripts.model_monitoring.featuredrift import FeatureDrift


def save_classification_prediction(data_frame):
    df = data_frame.to_dict("records")
    model_info = get_model_info("main-model-cpu")[0]
    model, created = ClassificationModel.objects.get_or_create(
        name=model_info["name"],
        version=model_info["version"],
        url=model_info["model_uri"],
        description=model_info["description"],
    )

    model_instances = [
        ClassificationPredictions(
            entry=Entry.objects.get(original_entry_id=int(record["entry_id"])),
            project=Project.objects.get(
                lead=Lead.objects.get(
                    entry=Entry.objects.get(original_entry_id=int(record["entry_id"]))
                )
            ),
            model=model,
            embeddings=record["embeddings"],
            subpillars_1d=record["subpillars_1d_pred"],
            sectors=record["sectors_pred"],
            subpillars_2d=record["subpillars_2d_pred"],
            age=record["age_pred"],
            gender=record["gender_pred"],
            affected_groups=record["affected_groups_pred"],
            specific_needs_groups=record["specific_needs_groups_pred"],
            severity=record["severity_pred"],
        )
        for record in df
    ]

    predictions = ClassificationPredictions.objects.bulk_create(model_instances)
    return predictions


def save_dataframe_to_model(dataframe, model_class):
    """
    Saves a pandas DataFrame into a Django model.
    Args:
        dataframe (pandas.DataFrame): The DataFrame to save.
        model_class (django.db.models.Model): The Django model class to save the DataFrame to.
    """
    for row in dataframe.itertuples(index=False):
        model_instance = model_class()
        for field in dataframe.columns:
            setattr(model_instance, field, getattr(row, field))
        model_instance.save()


def create_model_performance(df):
    modelperf = ModelPerformance(df)
    df1 = modelperf.project_wise_perf_metrics()
    save_dataframe_to_model(df1, ProjectWisePerfMatrices)

    df2 = modelperf.per_tag_perf_metrics()
    save_dataframe_to_model(df2, TagWisePerfMatrics)

    df3 = modelperf.all_projects_perf_metrics()
    save_dataframe_to_model(df3, AllProjectPerfMatrics)

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
        # create a data frame
        df = pd.DataFrame(
            list(
                Entry.objects.exclude(
                    original_entry_id__in=ClassificationPredictions.objects.values_list(
                        "entry__original_entry_id", flat=True
                    )
                )
                .order_by("-id")
                .values("original_entry_id", "excerpt_en", "original_af_tags")
            )[0:10]
        ).rename(
            columns={"original_entry_id": "entry_id", "excerpt_en": "excerpt"}
        )  # TODO remove [0:3]

        df["project_id"] = df.apply(set_project_id, axis=1)
        entry_df = df.drop(columns=["original_af_tags"])

        # generate output
        embeddings = ClassificationModelOutput(
            entry_df,
            endpoint_name="main-model-cpu",
            aws_region="us-east-1",
            batch_size=1,
            prediction_required=True,
            embeddings_required=True,
        )
        output_df = embeddings.generate_outputs()

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
        current_df = combined_df[['project_id', 'embeddings']]

        # create feature drift
        reference_data_path = "core/rup_file.csv"
        reference_data_df = pd.read_csv(reference_data_path)
        feature_drift = FeatureDrift(reference_data_df, current_df)
        feature_drift_df = feature_drift.compute_feature_drift(ref_n_samples=10, cur_n_samples=10)
        save_dataframe_to_model(feature_drift_df, ComputedFeatureDrift)

