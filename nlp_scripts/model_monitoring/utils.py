import boto3
from botocore.exceptions import ClientError
from typing import Dict, Tuple, Union

def get_model_info(endpoint_name: str) -> Tuple[Dict[str, str], Union[str, None]]:
    """
    Gets the model information
    Input: Endpoint name of the deployed model
    Output: Model information and error_msg(if any)
    """
    model_info = {}
    err_msg = None
    
    sg_client = boto3.client("sagemaker")

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
