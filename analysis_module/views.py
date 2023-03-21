import requests
import uuid
import json

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
from .models import AnalysisModuleRequest


def process_mock_request(request, type):

    MOCK_ENDPOINTS = {
        "topicmodel": "/mock/topicmodeling",
        "summarization": "/mock/summarization",
        "ngrams": "/mock/ngrams"
    }

    if not request.get("callback_url"):
        return Response({
            "message": "A callback URL must be provided"
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    req, code = request.get(
        "http://localhost:8081"+MOCK_ENDPOINTS.get(type), json=request
    )

    if code == 200:

        resp = {
            "client_id": request.get("client_id"),
            "type": type,
            "message": "Request has been successfully processed"
        }

        return Response(
            resp,
            status=status.HTTP_202_ACCEPTED,
        )
    
    else:
        return Response(
            {
                "message": req.json().get("status")
            },
            status=status.HTTP_400_BAD_REQUEST
        )


def process_request(serializer_model, request, type):

    serializer = serializer_model(data=request.data)
    serializer.is_valid(raise_exception=True)

    if serializer.data.get("mock"):
        return process_mock_request(
            request=serializer.data,
            type=type
        )

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
    status = AnalysisModuleRequest.objects.filter(
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
