import os
import json
import time
import requests
import boto3
import uuid
from celery import shared_task
from urllib.parse import urljoin
from typing import Dict, Literal, List, Any

from django.utils import timezone

from core.models import NLPRequest
from core_server.settings import (
    SUMMARIZATION_V2_ECS_ENDPOINT,
    TEXT_EXTRACTION_ECS_ENDPOINT,
    ENTRY_EXTRACTION_ECS_ENDPOINT
)
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
    nlp_request = NLPRequest.objects.get(unique_id=_id)

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
        nlp_request.status = NLPRequest.RequestStatus.FAILED
        nlp_request.save(update_fields=['status'])


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


def send_ecs_http_request(nlp_request: NLPRequest):
    ecs_id_param_name = get_ecs_id_param_name(nlp_request.type)
    url = get_ecs_url(nlp_request.type)
    if url is None:
        return
    data = nlp_request.request_params \
        if not ecs_id_param_name \
        else {
            **nlp_request.request_params,
            ecs_id_param_name: str(nlp_request.unique_id), # insert dinamically the unique id and respective task key 
        }
    try:
        response = requests.post(
            url,
            json=data,
            timeout=30,
        )
        if response.status_code < 200 or response.status_code > 299:
            logger.error(f"Failed response from ecs({url}): {response.text}", exc_info=True)
            nlp_request.status = NLPRequest.RequestStatus.FAILED
    except Exception:
        logger.error("Could not send http request to ecs: {url}", exc_info=True)
        nlp_request.status = NLPRequest.RequestStatus.FAILED
    nlp_request.last_process_attempted = timezone.now()
    nlp_request.process_attempts += 1
    nlp_request.save(update_fields=["status", "last_process_attempted", "process_attempts"])


def get_ecs_id_param_name(request_type: NLPRequest.FeaturesType):
    if request_type == NLPRequest.FeaturesType.SUMMARIZATION_V2:
        return "summarization_id"
    if request_type == NLPRequest.FeaturesType.TEXT_EXTRACTION:
        return "textextraction_id"
    if request_type == NLPRequest.FeaturesType.TEXT_EXTRACTION:
        return "entryextraction_id" # not needed probably, just to be in line with the rest. 
    return None


def get_ecs_url(request_type: NLPRequest.FeaturesType):
    if request_type == NLPRequest.FeaturesType.SUMMARIZATION_V2:
        return urljoin(SUMMARIZATION_V2_ECS_ENDPOINT, "/generate_report")
    elif request_type == NLPRequest.FeaturesType.TEXT_EXTRACTION:
        return urljoin(TEXT_EXTRACTION_ECS_ENDPOINT, "/extract_document")
    elif request_type == NLPRequest.FeaturesType.ENTRY_EXTRACTION:
        return urljoin(ENTRY_EXTRACTION_ECS_ENDPOINT, "/extract_entries")
    return None