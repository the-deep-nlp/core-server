import boto3
import uuid

from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from .serializers import (
    TopicModelDeepRequest, 
    DeepEntriesSerializer, 
    NgramsDeepRequest,
    StatusRequest
    )

from .utils import spin_ecs_container
from .models import AnalysisModuleStatus


def process_request(serializer_model, request, type):

    serializer = serializer_model(data=request.data)
    serializer.is_valid(raise_exception=True)
    unique_id = uuid.uuid4() #if not serializer.validated_data['callback_url'] else None

    _ = spin_ecs_container(
            task = type,
            params = serializer.data,
            _id = unique_id
        )
     
    resp = {
        "client_id": serializer.data.get("client_id"),
        "type": type,
        "message": "Request has been successfully processed"
    }

    if not serializer.data.get("callback_url"): resp.update({
            "unique_id": str(unique_id)
    })

    return Response(
        resp,
        status=status.HTTP_202_ACCEPTED,
    )


@api_view(["POST"])
def topic_modeling(request: Request):

    return process_request(
        TopicModelDeepRequest, request, "topicmodel"
    )


@api_view(["POST"])
def summarization(request: Request):

    return process_request(
        DeepEntriesSerializer, request, "summarization"
    )


@api_view(["POST"])
def ngrams(request: Request):

    return process_request(
        NgramsDeepRequest, request, "ngrams"
    )


@api_view(["GET"])
def status(request: Request):

    serializer = StatusRequest(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    unique_id = serializer.validated_data["unique_id"]
    status = AnalysisModuleStatus.objects.filter(
        unique_id=unique_id
    )

    if not status:
        return Response({
            "message": "Unrecored process"
        },
        status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(
            status,
            status=status.HTTP_200_OK
        )