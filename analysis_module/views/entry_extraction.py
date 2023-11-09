from copy import deepcopy
from django.db import transaction
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from core_server.settings import IS_MOCKSERVER
from core.models import NLPRequest
from analysis_module.serializers import EntryExtractionSerializer, ExtractionRequestTypeChoices
from analysis_module.utils import send_ecs_http_request
from analysis_module.mockserver import process_mock_request


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def entry_extraction(request: Request):
    serializer = EntryExtractionSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    data = deepcopy(serializer.validated_data) 
    items = data.pop("documents")
    if not items:
        return Response(
            {"message": "No documents present"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    req_type = NLPRequest.FeaturesType.ENTRY_EXTRACTION

    if serializer.validated_data.get("mock") or IS_MOCKSERVER:
        return process_mock_request(
            request=serializer.validated_data,
            request_type=req_type,
        )
    # Create NLPRequest objects
    nlp_reqs = []
    for doc in items:
        nlp_request = NLPRequest.objects.create(
            client_id=doc["client_id"],
            type=req_type,
            request_params={**doc, **data},
            created_by=request.user,
        )
        nlp_reqs.append(nlp_request)

        if serializer.validated_data["request_type"] == ExtractionRequestTypeChoices.USER:
            transaction.on_commit(lambda: send_ecs_http_request(nlp_request))

    resp = {
        "type": req_type,
        "message": "Request has been successfully queued",
        "request_ids": [str(x.unique_id) for x in nlp_reqs],
    }
    return Response(
        resp,
        status=status.HTTP_202_ACCEPTED,
    )
