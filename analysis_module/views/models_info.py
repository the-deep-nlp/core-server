from rest_framework.decorators import api_view, permission_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from analysis_module.mock_templates import MODELS_INFO_MOCK
from core_server.settings import IS_MOCKSERVER

from core_server.settings import (
    CLASSIFICATION_MODEL_ID,
    CLASSIFICATION_MODEL_VERSION,
    GEOLOCATION_MODEL_ID,
    GEOLOCATION_MODEL_VERSION,
    RELIABILITY_MODEL_ID,
    RELIABILITY_MODEL_VERSION
)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def models_detail(request: Request):
    """ Get the models information """
    if IS_MOCKSERVER:
        return Response(MODELS_INFO_MOCK)

    return Response({
        "classification_model": {
            "id": CLASSIFICATION_MODEL_ID,
            "version": CLASSIFICATION_MODEL_VERSION
        },
        "geolocation_model": {
            "id": GEOLOCATION_MODEL_ID,
            "version": GEOLOCATION_MODEL_VERSION
        },
        "reliablity_model": {
            "id": RELIABILITY_MODEL_ID,
            "version": RELIABILITY_MODEL_VERSION
        }
    })
