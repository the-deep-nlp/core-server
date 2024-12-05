import logging
from django.db import transaction
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from core_server.settings import IS_MOCKSERVER
from core.models import NLPRequest
from analysis_module.serializers import PredictionRequestSerializerV2
# from analysis_module.mockserver import MOCK_ENTRY_CLASSIFICATION
from analysis_module.utils import send_classification_tags_llm
from analysis_module.mockserver import process_mock_request


logger = logging.getLogger(__name__)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def entry_classification(request: Request):

    serializer = PredictionRequestSerializerV2(data=request.data)
    serializer.is_valid(raise_exception=True)

    entries = serializer.validated_data["entries"]
    req_type = NLPRequest.FeaturesType.ENTRY_CLASSIFICATION_LLM

    if serializer.validated_data.get("mock") or IS_MOCKSERVER:
        return process_mock_request(
            request=serializer.validated_data,
            request_type=req_type
        )
    if not entries:
        return Response({})
    # Create a NLPRequest object
    nlp_request = NLPRequest.objects.create(
        client_id=entries[0]["client_id"],
        type=NLPRequest.FeaturesType.ENTRY_CLASSIFICATION_LLM,
        request_params=serializer.validated_data,
        created_by=request.user,
    )

    resp = {
        "type": req_type,
        "message": "Request has been successfully queued.",
        "request_ids": nlp_request.unique_id
    }

    transaction.on_commit(
        lambda: send_classification_tags_llm.delay(nlp_request_id=nlp_request.pk)
    )

    return Response(
        resp,
        status=status.HTTP_202_ACCEPTED,
    )
