from django.http import JsonResponse
import pandas as pd

from nlp_scripts.model_monitoring.utils import get_model_info
from .models import (
    Entry,
    Lead,
    Project,
    ClassificationPredictions,
    ClassificationModel,
)
from nlp_scripts.model_monitoring.generate_outputs import ClassificationModelOutput
from nlp_scripts.model_monitoring.model_performance import ModelPerformance


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


def prepare_model_performance_df(df):
    modelperf = ModelPerformance(df)
    df1 = modelperf.project_wise_perf_metrics()
    # print(df1.columns)
    # print(df1.iloc[0])
    df2 = modelperf.per_tag_perf_metrics()
    # print(df2.columns)
    df3 = modelperf.all_projects_perf_metrics()
    # print(df3)
    df4 = modelperf.calculate_ratios()
    # print(df4)
    df5 = modelperf.per_project_calc_ratios()
    # print(df5)


def set_project_id(row):
    project = Project.objects.get(
        lead=Lead.objects.get(
            entry=Entry.objects.get(original_entry_id=row["entry_id"])
        )
    )
    return project.id


def test_celery(request):
    # create a data frame
    df = pd.DataFrame(
                    "entry__original_entry_id", flat=True
            )
            .order_by("-id")
            .values("original_entry_id", "excerpt_en", "original_af_tags")
        )[0:3]
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
    combined_df = combined_df.drop(
        columns=[
            "embeddings",
            "age_pred",
            "gender_pred",
            "affected_groups_pred",
            "specific_needs_groups_pred",
            "severity_pred",
            "generated_at",
        ]
    )
    mod_perf_df = prepare_model_performance_df(combined_df)

    return JsonResponse({"test": "test"})
