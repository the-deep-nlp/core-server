import os
import json
import time
import requests
import boto3
import uuid
import logging
from celery import shared_task
from urllib.parse import urljoin
from typing import Dict, Literal, List, Any
from nlp_scripts.model_prediction.model_prediction import ModelTagsPrediction
from nlp_scripts.model_prediction.llm.model_prediction import LLMTagsPrediction

from django.utils import timezone

from core.models import NLPRequest
from core_server.settings import (
    SUMMARIZATION_V3_ECS_ENDPOINT,
    TEXT_EXTRACTION_ECS_ENDPOINT,
    ENTRYEXTRACTION_ECS_ENDPOINT,
    ENTRYEXTRACTION_LLM_ECS_ENDPOINT,
    GEOLOCATION_ECS_ENDPOINT,
    TOPICMODEL_ECS_ENDPOINT
)

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


def get_geolocations(excerpts: List[str], req_timeout: int = 60):
    """ Get geolocations from excerpts by requesting from geolocation module """
    if not GEOLOCATION_ECS_ENDPOINT:
        logging.error("The geolocation module endpoint not found.")
        return None
    data = {"entries_list": excerpts}
    try:
        response = requests.post(
            GEOLOCATION_ECS_ENDPOINT + "/get_geolocations",
            json=data,
            timeout=req_timeout
        )
        return response.json()
    except requests.exceptions.Timeout as terr:
        logging.error("Request timeout to the geolocation endpoint. %s", str(terr))
    except requests.exceptions.ConnectionError as cerr:
        logging.error("Request connection error occurred. %s", str(cerr))
    return None


@shared_task
def send_classification_tags(nlp_request_id: int, version: str = "v1"):
    nlp_request = NLPRequest.objects.get(pk=nlp_request_id)
    predictor = ModelTagsPrediction()
    entries_dict = nlp_request.request_params["entries"]
    pred_data = predictor(entries_dict)

    entries_only = [item["entry"] for item in entries_dict]
    geolocations = get_geolocations(entries_only)

    output_data = {
        "client_id": entries_dict[0]["client_id"],
        "model_tags": pred_data,
        "geolocations": geolocations[0]["locations"] if geolocations else [],
        "model_info": {
            "id": "all_tags_model",
            "version": "1.0.0"
        },
        "prediction_status": True
    }

    callback_url = nlp_request.request_params["callback_url"]

    try:
        response = requests.post(
            callback_url,
            json=output_data,
            timeout=30
        )
        if response.status_code < 200 or response.status_code > 299:
            logger.error(f"Failed to receive an acknowledgement. Status code: {response.status_code}")
    except Exception:
        logger.error("Could not send http request on callback url : {callback_url}", exc_info=True)


@shared_task
def send_classification_tags_llm(nlp_request_id: int, version: str = "v1"):
    nlp_request = NLPRequest.objects.get(pk=nlp_request_id)
    predictor = LLMTagsPrediction(analysis_framework_id=nlp_request.request_params['af_id'])
    entries_dict = nlp_request.request_params["entries"]
    pred_data = predictor.predict(entries_dict)[0]

    entries_only = [item["entry"] for item in entries_dict]
    geolocations = get_geolocations(entries_only)

    output_data = {
        "client_id": entries_dict[0]["client_id"],
        "model_tags": pred_data,
        "geolocations": geolocations[0]["locations"] if geolocations else [],
        "model_info": {
            "id": "llm_model",
            "version": "1.0.0"
        },
        "prediction_status": True
    }

    callback_url = nlp_request.request_params["callback_url"]

    try:
        response = requests.post(
            callback_url,
            json=output_data,
            timeout=30
        )
        if response.status_code < 200 or response.status_code > 299:
            logger.error(f"Failed to receive an acknowledgement. Status code: {response.status_code}")
    except Exception:
        logger.error("Could not send http request on callback url : {callback_url}", exc_info=True)


def send_ecs_http_request(nlp_request: NLPRequest):
    ecs_id_param_name = get_ecs_id_param_name(nlp_request.type)
    url = get_ecs_url(nlp_request.type)
    if url is None:
        return
    data = nlp_request.request_params \
        if not ecs_id_param_name \
        else {
            **nlp_request.request_params,
            ecs_id_param_name: str(nlp_request.unique_id),  # insert dinamically the unique id and respective task key
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
    mapper = {
        NLPRequest.FeaturesType.TOPICMODEL: "topicmodel_id",
        NLPRequest.FeaturesType.GEOLOCATION: "geolocation_id",
        NLPRequest.FeaturesType.ENTRY_EXTRACTION: "entryextraction_id",
        NLPRequest.FeaturesType.ENTRY_EXTRACTION_LLM: "entryextraction_id",
        NLPRequest.FeaturesType.TEXT_EXTRACTION: "textextraction_id",
        NLPRequest.FeaturesType.SUMMARIZATION_V3: "summarization_id"
    }
    return mapper.get(request_type, None)


def get_ecs_url(request_type: NLPRequest.FeaturesType):
    mapper = {
        NLPRequest.FeaturesType.TOPICMODEL: urljoin(TOPICMODEL_ECS_ENDPOINT, "/get_excerpt_clusters"),
        NLPRequest.FeaturesType.GEOLOCATION: urljoin(GEOLOCATION_ECS_ENDPOINT, "/get_geolocations"),
        NLPRequest.FeaturesType.ENTRY_EXTRACTION: urljoin(ENTRYEXTRACTION_ECS_ENDPOINT, "/extract_entries"),
        NLPRequest.FeaturesType.ENTRY_EXTRACTION_LLM: urljoin(ENTRYEXTRACTION_LLM_ECS_ENDPOINT, "/extract_entries_llm"),
        NLPRequest.FeaturesType.TEXT_EXTRACTION: urljoin(TEXT_EXTRACTION_ECS_ENDPOINT, "/extract_document"),
        NLPRequest.FeaturesType.SUMMARIZATION_V3: urljoin(SUMMARIZATION_V3_ECS_ENDPOINT, "/generate_report")
    }
    return mapper.get(request_type, None)
