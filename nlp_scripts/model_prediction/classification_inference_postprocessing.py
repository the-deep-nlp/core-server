import boto3
import pandas as pd
import warnings
import logging

from botocore.exceptions import ClientError

warnings.filterwarnings("ignore")
client = boto3.session.Session().client("sagemaker-runtime", region_name="us-east-1")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_outputs_from_endpoint(test_df: pd.DataFrame, endpoint_name: str):
    inputs = test_df[["excerpt"]]
    inputs["return_type"] = "default_analyis"
    inputs["analyis_framework_id"] = "all"

    # kw for interpretability
    inputs["interpretability"] = False
    # minimum ratio between proba and threshold to perform interpretability
    inputs["ratio_interpreted_labels"] = 0.5
    inputs["attribution_type"] = "Layer DeepLift"

    # predictions
    inputs["return_prediction_labels"] = True

    # kw for embeddings
    inputs["output_backbone_embeddings"] = False
    inputs["pooling_type"] = "['cls', 'mean_pooling']"
    inputs["finetuned_task"] = "['first_level_tags', 'secondary_tags', 'subpillars']"
    inputs["embeddings_return_type"] = "array"

    backbone_inputs_json = inputs.to_json(orient="split")
    try:
        response = client.invoke_endpoint(
            EndpointName=endpoint_name,
            Body=backbone_inputs_json,
            ContentType="application/json; format=pandas-split",
        )
        output = response["Body"].read().decode("ascii")
    except ClientError as cexc:
        logger.error("Error occurred while invoking the sagemaker endpoint. %s", str(cexc))
        raise cexc

    return output
