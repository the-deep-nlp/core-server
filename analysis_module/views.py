import requests
import uuid
import json
import os

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
from .mockserver import topicmodelingmodel, ngramsmodel, summarizationmodel


def process_mock_request(request, type):

    if type=="topicmodel":
        response, code = topicmodelingmodel(request)
    elif type=="summarization":
        response, code = summarizationmodel(request)
    elif type=="ngrams":
        response, code = ngramsmodel(request)

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
                "message": response["status"]
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
def processing_status(request: Request, unique_id: str):
    
    unique_id = request.query_params.get("unique_id")
    status = AnalysisModuleRequest.objects.filter(unique_id=unique_id).first()

    if not status:
        return Response({
            "message": "Unrecorded process"
        },
        status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(
            status,
            status=status.HTTP_200_OK
        )
