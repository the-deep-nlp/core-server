import boto3
from botocore.exceptions import ClientError
from typing import Dict, Tuple, Union

def get_model_info(endpoint_name: str) -> Tuple[Dict[str, str], Union[str, None]]:
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

    print("Model info",model_info)
    return model_info, err_msg
