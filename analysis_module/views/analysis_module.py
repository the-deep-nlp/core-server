import requests
from typing import Literal
from urllib.parse import urljoin

from django.db import transaction
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from analysis_module.serializers import (
    TopicModelDeepRequest,
    EntriesSerializer,
    NgramsRequest,
)
from core_server.settings import IS_MOCKSERVER, SUMMARIZATION_V2_ECS_ENDPOINT

from core.models import NLPRequest
from analysis_module.utils import spin_ecs_container, send_ecs_http_request
from analysis_module.mockserver import topicmodeling_model, ngrams_model, summarization_model, geolocation_model

RequestType = Literal["topicmodel", "ngrams", "summarization", "geolocation"]

TYPE_ACTIONS_MOCK = {
    "topicmodel": topicmodeling_model,
    "summarization": summarization_model,
    "ngrams": ngrams_model,
    "geolocation": geolocation_model,
}


def process_mock_request(request: dict, request_type: str):
    action = TYPE_ACTIONS_MOCK.get(request_type)
    if action is None:
        raise ValidationError("Invalid request type")

    response, code = action(request)

    if code == 200:
        resp = {
            "client_id": request.get("client_id"),
            "type": request_type,
            "message": "Request has been successfully processed",
        }

        return Response(
            resp,
            status=status.HTTP_202_ACCEPTED,
        )

    else:
        return Response(
            {"message": response["status"]},
            status=status.HTTP_400_BAD_REQUEST,
        )


def process_request(
    serializer_model,
    request: Request,
    request_type: RequestType,
):
    serializer = serializer_model(data=request.data)
    serializer.is_valid(raise_exception=True)

    if serializer.validated_data.get("mock") or IS_MOCKSERVER:
        return process_mock_request(request=serializer.validated_data, request_type=request_type)

    nlp_request = NLPRequest.objects.create(
        client_id=serializer.validated_data["client_id"],
        type=request_type,
        request_params=serializer.validated_data,
    )
    transaction.on_commit(lambda: spin_ecs_container.delay(
        task=request_type,
        params=serializer.data,
        _id=nlp_request.unique_id,
    ))

    resp = {
        "client_id": serializer.data.get("client_id"),
        "type": request_type,
        "message": "Request has been successfully processed",
        "request_id": str(nlp_request.unique_id),
    }
    return Response(
        resp,
        status=status.HTTP_202_ACCEPTED,
    )


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def topic_modeling(request: Request):
    return process_request(TopicModelDeepRequest, request, "topicmodel")


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def summarization(request: Request):
    return process_request(EntriesSerializer, request, "summarization")


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def summarization_v2(request: Request):
    serializer = EntriesSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    if serializer.validated_data.get("mock") or IS_MOCKSERVER:
        return process_mock_request(request=serializer.validated_data, request_type="summarization")

    nlp_request = NLPRequest.objects.create(
        client_id=serializer.validated_data["client_id"],
        type="summarization",
        request_params=serializer.validated_data,
    )
    unique_id = str(nlp_request.unique_id)
    transaction.on_commit(lambda: send_ecs_http_request.delay(
        url=urljoin(SUMMARIZATION_V2_ECS_ENDPOINT, "/generate_report"),
        request_id=unique_id,
        data=serializer.validated_data,
        ecs_id_param_name="summarization_id"
    ))
    resp = {
        "client_id": serializer.data.get("client_id"),
        "type": "summaraization",
        "message": "Request has been successfully processed",
        "request_id": unique_id,
    }
    return Response(
        resp,
        status=status.HTTP_202_ACCEPTED,
    )


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def ngrams(request: Request):
    return process_request(NgramsRequest, request, "ngrams")


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def geolocation(request: Request):
    return process_request(EntriesSerializer, request, "geolocation")


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def request_status(request: Request, unique_id: str):
    unique_id = request.query_params.get("unique_id")
    status = NLPRequest.objects.filter(unique_id=unique_id).first()

    if not status:
        return Response(
            {"message": "Unrecorded process"}, status=status.HTTP_404_NOT_FOUND
        )
    else:
        return Response(
            status,
            status=status.HTTP_200_OK
        )
