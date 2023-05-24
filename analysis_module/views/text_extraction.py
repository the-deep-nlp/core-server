from django.db import transaction
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from core_server.settings import IS_MOCKSERVER
from core.models import NLPRequest
from analysis_module.serializers import TextExtractionSerializer, ExtractionRequestTypeChoices
from analysis_module.utils import send_ecs_http_request


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def text_extraction(request: Request):
    serializer = TextExtractionSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    items = serializer.validated_data["documents"]
    if not items:
        return Response({"extracted_documents": []})
    req_type = NLPRequest.FeaturesType.TEXT_EXTRACTION

    if serializer.validated_data.get("mock") or IS_MOCKSERVER:
        # TODO:
        return process_mock_request(
            request=serializer.validated_data,
            request_type=req_type,
        )
    # Create a NLPRequest object
    nlp_request = NLPRequest.objects.create(
        client_id=items[0]["client_id"],
        type=req_type,
        request_params=serializer.validated_data,
        created_by=request.user,
    )
    # If user triggered, call ecs immediately, if not cron job will handle
    # but make sure send_ecs_http_request will accordingly updated the last_process_attempted value
    if serializer.validated_data["request_type"] == ExtractionRequestTypeChoices.USER:
        transaction.on_commit(lambda: send_ecs_http_request(nlp_request))

    resp = {
        "type": req_type,
        "message": "Request has been successfully queued",
        "request_id": str(nlp_request.unique_id),
    }
    return Response(
        resp,
        status=status.HTTP_202_ACCEPTED,
    )
