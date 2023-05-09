from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from analysis_module.serializers import TagsMappingRequestSerializer
from core.models import NLPRequest
from nlp_scripts.model_prediction.tags_mapping import AF2NLPMapping

import logging

logger = logging.getLogger(__name__)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def tags_mapping(request: Request):
    serializer = TagsMappingRequestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    items = serializer.validated_data["items"]
    if not items:
        return Response({"tags_mapping": []})
    # Create a NLPRequest object
    nlp_request = NLPRequest.objects.create(
        client_id=items[0]["client_id"],
        type=NLPRequest.FeaturesType.TAGS_MAPPING,
        request_params=serializer.validated_data,
    )
    af2nlp_map = AF2NLPMapping()
    try:
        resp_data = af2nlp_map(items, full_output=False)
    except Exception:
        logger.warning(
            f"Failed processing request for nlp request {nlp_request.id}",
            exc_info=True,
        )
        nlp_request.status = NLPRequest.RequestStatus.FAILED
        return Response({}, status=status.HTTP_400_BAD_REQUEST)
    else:
        nlp_request.status = NLPRequest.RequestStatus.SUCCESS
    return Response(resp_data)
