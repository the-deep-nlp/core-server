import os
import json
import time
import requests
import boto3
import uuid
from celery import shared_task
from typing import Dict, Literal, List, Any

from core.models import NLPRequest

import logging

logger = logging.getLogger(__name__)


TASK_MAPPINGS: Dict = {
    "ngrams": {
        "ecs_cluster_id": "NGRAMS_ECS_CLUSTER_ID",
        "ecs_task_definition_arn": "NGRAMS_ECS_TASK_DEFN_ARN",
        "ecs_container_name": "NGRAMS_ECS_CONTAINER_NAME",
        "vpc_private_subnet": "NGRAMS_VPC_PRIVATE_SUBNET",
        "unique_id": "NGRAMS_ID",
    },
    "topicmodel": {
        "ecs_cluster_id": "TOPICMODEL_ECS_CLUSTER_ID",
        "ecs_task_definition_arn": "TOPICMODEL_ECS_TASK_DEFN_ARN",
        "ecs_container_name": "TOPICMODEL_ECS_CONTAINER_NAME",
        "vpc_private_subnet": "TOPICMODEL_VPC_PRIVATE_SUBNET",
        "unique_id": "TOPICMODEL_ID",
    },
    "summarization": {
        "ecs_cluster_id": "SUMMARIZATION_ECS_CLUSTER_ID",
        "ecs_task_definition_arn": "SUMMARIZATION_ECS_TASK_DEFN_ARN",
        "ecs_container_name": "SUMMARIZATION_ECS_CONTAINER_NAME",
        "vpc_private_subnet": "SUMMARIZATION_VPC_PRIVATE_SUBNET",
        "unique_id": "SUMMARIZATION_ID",
    },
    "geolocation": {
        "ecs_cluster_id": "GEOLOCATION_ECS_CLUSTER_ID",
        "ecs_task_definition_arn": "GEOLOCATION_ECS_TASK_DEFN_ARN",
        "ecs_container_name": "GEOLOCATION_ECS_CONTAINER_NAME",
        "vpc_private_subnet": "GEOLOCATION_VPC_PRIVATE_SUBNET",
        "unique_id": "GEOLOCATION_ID",
    },
}


def create_params(
    params: Dict, mapping: Dict, _id: uuid.uuid4 = None
) -> List[Dict[str, str]]:
    _params = []
    for k, v in params.items():
        if isinstance(v, dict):
            for k1, v1 in v.items():
                _params.append(
                    {
                        "name": k1.upper(),
                        "value": str(v1),
                    }
                )
        else:
            _params.append(
                {"name": k.upper(), "value": str(v)}
            )

    # if not params.get('callback_url'):
    # if not _id:
    #   raise ValueError("Need an unique UUID if no callback URL is provided")
    _params.append({"name": mapping.get("unique_id"), "value": str(_id)})

    return _params


@shared_task
def spin_ecs_container(
    task: Literal["ngrams", "topicmodel", "summarization", "geolocation"],
    params,
    _id=None,
) -> Any:
    am_request = NLPRequest.objects.get(unique_id=_id)

    try:
        ecs_client = boto3.client("ecs", region_name=os.getenv("AWS_REGION"))
        mapping = TASK_MAPPINGS.get(task)

        def _mapping_value(val):
            if not mapping:
                return ""
            env_var = mapping.get(val)
            return os.environ.get(env_var or "")

        overrides_params = {
            "containerOverrides": [
                {
                    "name": f"{_mapping_value('ecs_container_name')}-{os.getenv('ENVIRONMENT')}",
                    "command": ["python", "app.py"],
                    "environment": create_params(params, mapping, _id),
                },
            ],
        }
        response = ecs_client.run_task(
            cluster=_mapping_value("ecs_cluster_id"),
            launchType="FARGATE",
            taskDefinition=_mapping_value("ecs_task_definition_arn"),
            count=1,
            platformVersion="LATEST",
            networkConfiguration={
                "awsvpcConfiguration": {
                    "subnets": [_mapping_value("vpc_private_subnet")],
                    "assignPublicIp": "DISABLED",
                }
            },
            overrides=overrides_params,
        )
        return response
    except Exception:
        logger.error("Error spinning ecs_container", exc_info=True)
        am_request.status = AnalysisModuleRequest.RequestStatus.FAILED
        am_request.save(update_fields=['status'])


@shared_task
def send_callback_url_request(callback_url: str, client_id: str, filepath: str, status: int) -> Any:
    """send callback url"""

    time.sleep(1)
    if callback_url:
        response_callback_url = requests.post(
            callback_url,
            json={
                "client_id": client_id,
                "presigned_s3_url": filepath,
                "status": status,
            },
            timeout=30,
        )
        if response_callback_url.status_code == 200:
            logging.info("Request sent successfully.")
            return json.dumps({"status": "Request sent successfully."})
        else:
            logging.info(
                f"Some errors occurred. StatusCode: {response_callback_url.status_code}"
            )
            return json.dumps(
                {
                    "status": f"Error occurred with statuscode: {response_callback_url.status_code}"
                }
            )

    logging.error("No callback url found.")
    return json.dumps({"status": "No callback url found."}), 400
