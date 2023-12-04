from django.db import transaction
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from core_server.settings import IS_MOCKSERVER
from core.models import NLPRequest
from analysis_module.serializers import TagsMappingRequestSerializer, PredictionRequestSerializer
from analysis_module.mockserver import MOCK_ENTRY_CLASSIFICATION
from analysis_module.utils import send_classification_tags
from nlp_scripts.model_prediction.tags_mapping import AF2NLPMapping
from nlp_scripts.model_prediction.model_prediction import ModelTagsPrediction
from nlp_scripts.model_prediction.all_tags_mapping import get_vf_list

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
        created_by=request.user,
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
    nlp_request.save(update_fields=['status'])
    return Response({"tags_mapping": resp_data})


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def nlp_tags(request: Request):
    return Response(get_vf_list())


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def entry_classification(request: Request):
    serializer = PredictionRequestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    entries = serializer.validated_data["entries"]
    if serializer.validated_data.get("mock") or IS_MOCKSERVER:
        data = MOCK_ENTRY_CLASSIFICATION
        data.update({
            "client_id": entries[0]["client_id"]
        })
        return Response(data)
    if not entries:
        return Response({})
    # Create a NLPRequest object
    nlp_request = NLPRequest.objects.create(
        client_id=entries[0]["client_id"],
        type=NLPRequest.FeaturesType.ENTRY_CLASSIFICATION,
        request_params=serializer.validated_data,
        created_by=request.user,
    )

    req_type = NLPRequest.FeaturesType.ENTRY_CLASSIFICATION

    resp = {
        "type": req_type,
        "message": "Request has been successfully queued.",
        "request_ids": nlp_request.unique_id
    }

    transaction.on_commit(
        lambda: send_classification_tags.delay(nlp_request_id=nlp_request.pk)
    )
    #transaction.on_commit(lambda: send_classification_tags(nlp_request=nlp_request))

    return Response(
        resp,
        status=status.HTTP_202_ACCEPTED,
    )


    # predictor = ModelTagsPrediction()
    # try:
    #     entries_lst = [e["entry"] for e in entries]
        
    #     pred_data = predictor(entries_lst)
    #     resp_data = {
    #         "client_id": entries[0]["client_id"],
    #         "model_preds": {
    #             "classification_tags": pred_data
    #         },
    #         "prediction_status": NLPRequest.RequestStatus.SUCCESS,
    #     }
    #     logger.info("resp data on predictions")
    #     logger.info(resp_data)
    # except Exception:
    #     logger.warning(
    #         f"Failed processing request for nlp request {nlp_request.id}",
    #         exc_info=True,
    #     )
    #     nlp_request.status = NLPRequest.RequestStatus.FAILED
    #     return Response({}, status=status.HTTP_400_BAD_REQUEST)
    # else:
    #     nlp_request.status = NLPRequest.RequestStatus.SUCCESS
    # nlp_request.save(update_fields=['status'])
    # return Response(resp_data)
