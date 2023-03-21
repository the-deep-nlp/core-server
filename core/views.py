from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def token_auth_dummy_view(request: Request):
    return Response({})
