import requests
from typing import Literal

from django.db import transaction
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    TopicModelDeepRequest,
    DeepEntriesSerializer,
    NgramsDeepRequest,
)
from core_server.settings import IS_MOCKSERVER

from core.models import NLPRequest
from .utils import spin_ecs_container
from .mockserver import topicmodeling_model, ngrams_model, summarization_model, geolocation_model


TYPE_ACTIONS = {
    "topicmodel": topicmodeling_model,
    "summarization": summarization_model,
    "ngrams": ngrams_model,
    "geolocation": geolocation_model,
}


def process_mock_request(request: dict, request_type: str):
    action = TYPE_ACTIONS.get(request_type)
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


# TODO: better types for request_type param
def process_request(
    serializer_model,
    request: Request,
    request_type: Literal["topicmodel", "ngrams", "summarization"]
):
    serializer = serializer_model(data=request.data)
    serializer.is_valid(raise_exception=True)

    if serializer.validated_data.get("mock") or IS_MOCKSERVER:
        return process_mock_request(request=serializer.validated_data, request_type=request_type)

    am_request = NLPRequest.objects.create(
        client_id=serializer.validated_data["client_id"],
        type=request_type,
        request_params=serializer.validated_data,
    )
    transaction.on_commit(lambda: spin_ecs_container.delay(
        task=request_type,
        params=serializer.data,
        _id=am_request.unique_id,
    ))

    resp = {
        "client_id": serializer.data.get("client_id"),
        "type": request_type,
        "message": "Request has been successfully processed",
    }

    if not serializer.data.get("callback_url"):
        resp.update({"unique_id": str(am_request.unique_id)})

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
    return process_request(DeepEntriesSerializer, request, "summarization")


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def ngrams(request: Request):
    return process_request(NgramsDeepRequest, request, "ngrams")


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def geolocation(request: Request):
    return process_request(DeepEntriesSerializer, request, "geolocation")


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
