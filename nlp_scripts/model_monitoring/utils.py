import json
from ast import literal_eval
from typing import Dict, List, Tuple, Optional, Any
import boto3
from botocore.exceptions import ClientError

from .constants import CATEGORIES


def get_model_info(
    endpoint_name: str,
    aws_access_key_id: Optional[str],
    aws_secret_access_key: Optional[str],
    region_name: str = "us-east-1",
) -> Tuple[Dict[str, str], Optional[str]]:
    """
    Gets the model information
    Input: Endpoint name of the deployed model
    Output: Returns a tuple that has Model information and error_msg.
    The model information is a dictionary which has keys: name, description, model_uri, version
    Example: ({'name': 'classification_model', 'description': 'Model for classifying several tags',
    'model_uri': 's3://deep-mlflow-artifact/30/xxx/artifacts/two_steps_models', 'version': '1.0',
    'reference_train_data': 's3://models-monitoring/drifts/xx/ref_train_xx.csv'}, None)
    In case of an error, error_msg is populated with an error description and model information is an empty dict.
    """
    model_info = {}
    err_msg = None

    sg_client = boto3.client(
        "sagemaker",
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=region_name,
    )

    try:
        response = sg_client.describe_endpoint(EndpointName=endpoint_name)
        for prod_variant in response["ProductionVariants"]:
            model_name = prod_variant["VariantName"]
            model_desc_response = sg_client.describe_model(ModelName=model_name)
            model_arn = model_desc_response["ModelArn"]
            model_tags = sg_client.list_tags(ResourceArn=model_arn)
            if "Tags" in model_tags:
                for tag in model_tags["Tags"]:
                    if "Key" in tag:
                        model_info[tag["Key"]] = tag["Value"]
    except ClientError as err:
        err_msg = err.response["Error"]["Message"]

    return model_info, err_msg


def group_tags(tags_collection: Dict) -> Dict[str, List[str]]:
    """
    Group tags into different categories
    """
    tags_dict = {}
    for key in tags_collection.keys():
        try:
            first_key, second_key, *_ = key.split("->")
        except ValueError:
            continue
        if second_key.lower() in CATEGORIES:
            if second_key not in tags_dict:
                tags_dict[second_key] = []
            tags_dict[second_key].append(key)
        if first_key.lower() in ["subsectors", "subpillars_1d", "subpillars_2d"]:
            if first_key not in tags_dict:
                tags_dict[first_key] = []
            tags_dict[first_key].append(key)
    return tags_dict


def invoke_model_endpoint(
    backbone_inputs: dict,
    sagemaker_model: boto3.client,
    endpoint_name: str,
    content_type: str = "application/json; format=pandas-split",
) -> Dict:
    """
    Invokes the sagemaker model endpoint
    """
    try:
        response = sagemaker_model.invoke_endpoint(
            EndpointName=endpoint_name, Body=backbone_inputs, ContentType=content_type
        )
        return json.loads(response["Body"].read().decode("ascii"))
    except ClientError as error:
        raise Exception(error)


def try_literal_eval(x: Any) -> Any:
    try:
        return literal_eval(x)
    except ValueError:
        return x
