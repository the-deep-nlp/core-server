from typing import Literal

from django.db import transaction
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from analysis_module.serializers import (
    TopicModelDeepRequest,
    EntriesSerializer,
    NgramsRequest,
)
from core_server.settings import IS_MOCKSERVER
from core.models import NLPRequest
from analysis_module.utils import spin_ecs_container
from analysis_module.mockserver import process_mock_request

RequestType = Literal["topicmodel", "ngrams", "summarization", "geolocation"]


def process_request(
    serializer_model,
    request: Request,
    request_type: RequestType,
):
    serializer = serializer_model(data=request.data)
    serializer.is_valid(raise_exception=True)

    if serializer.validated_data.get("mock") or IS_MOCKSERVER:
        return process_mock_request(
            request=serializer.validated_data, request_type=request_type
        )

    nlp_request = NLPRequest.objects.create(
        client_id=serializer.validated_data["client_id"],
        type=request_type,
        request_params=serializer.validated_data,
        created_by=request.user,
    )
    transaction.on_commit(
        lambda: spin_ecs_container.delay(
            task=request_type,
            params=serializer.data,
            _id=nlp_request.unique_id,
        )
    )

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
        return process_mock_request(
            request=serializer.validated_data,
            request_type=NLPRequest.FeaturesType.SUMMARIZATION_V2,
        )

    nlp_request = NLPRequest.objects.create(
        client_id=serializer.validated_data["client_id"],
        type=NLPRequest.FeaturesType.SUMMARIZATION_V2,
        request_params=serializer.validated_data,
        created_by=request.user,
    )
    resp = {
        "client_id": serializer.data.get("client_id"),
        "type": NLPRequest.FeaturesType.SUMMARIZATION_V2,
        "message": "Request has been successfully processed",
        "request_id": str(nlp_request.unique_id),
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
        return Response(status, status=status.HTTP_200_OK)
