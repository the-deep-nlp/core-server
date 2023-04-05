import os
import boto3
import uuid
from celery import shared_task
from typing import Dict, Literal, List, Any

from analysis_module.models import AnalysisModuleRequest

import logging

logger = logging.getLogger(__name__)


TASK_MAPPINGS: Dict = {
    "ngrams": {
        "ecs_cluster_id": "NGRAMS_ECS_CLUSTER_ID",
        "ecs_task_definition_arn": "NGRAMS_ECS_TASK_DEFN_ARN",
        "ecs_container_name": "NGRAMS_ECS_CONTAINER_NAME",
        "vpc_private_subnet": "NGRAMS_VPC_PRIVATE_SUBNET",
        "no_callback_id": "NGRAMS_ID",
    },
    "topicmodel": {
        "ecs_cluster_id": "TOPICMODEL_ECS_CLUSTER_ID",
        "ecs_task_definition_arn": "TOPICMODEL_ECS_TASK_DEFN_ARN",
        "ecs_container_name": "TOPICMODEL_ECS_CONTAINER_NAME",
        "vpc_private_subnet": "TOPICMODEL_VPC_PRIVATE_SUBNET",
        "no_callback_id": "TOPICMODEL_ID",
    },
    "summarization": {
        "ecs_cluster_id": "SUMMARIZATION_ECS_CLUSTER_ID",
        "ecs_task_definition_arn": "SUMMARIZATION_ECS_TASK_DEFN_ARN",
        "ecs_container_name": "SUMMARIZATION_ECS_CONTAINER_NAME",
        "vpc_private_subnet": "SUMMARIZATION_VPC_PRIVATE_SUBNET",
        "unique_id": "SUMMARIZATION_ID",
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
                        "value": str(v1) if isinstance(v, bool) else v1,
                    }
                )
        else:
            _params.append(
                {"name": k.upper(), "value": str(v) if isinstance(v, bool) else v}
            )

    # if not params.get('callback_url'):
    # if not _id:
    #   raise ValueError("Need an unique UUID if no callback URL is provided")
    _params.append({"name": mapping.get("unique_id"), "value": str(_id)})

    return _params


@shared_task
def spin_ecs_container(
    task: Literal["ngrams", "topicmodel", "summarization"],
    params,
    _id=None,
) -> Any:
    am_request = AnalysisModuleRequest.objects.get(unique_id=_id)

    try:
        ecs_client = boto3.client("ecs", region_name=os.getenv("AWS_REGION"))
        mapping = TASK_MAPPINGS.get(task)

        response = ecs_client.run_task(
            cluster=mapping.get("ecs_cluster_id"),
            launchType="FARGATE",
            taskDefinition=mapping.get("ecs_task_definition_arn"),
            count=1,
            platformVersion="LATEST",
            networkConfiguration={
                "awsvpcConfiguration": {
                    "subnets": [mapping.get("vpc_private_subnet")],
                    "assignPublicIp": "DISABLED",
                }
            },
            overrides={
                "containerOverrides": [
                    {
                        "name": f"{mapping.get('ecs_container_name')}-{os.getenv('ENVIRONMENT')}",
                        "command": ["python", "app.py"],
                        "environment": create_params(params, mapping, _id),
                    },
                ],
            },
        )
        return response
    except Exception:
        import traceback
        logger.error("Error spinning ecs_container", exc_info=True)
        am_request.status = AnalysisModuleRequest.RequestStatus.FAILED
        am_request.error = traceback.format_exc()
        am_request.save(update_fields=['status', 'error'])
