from django.http import Http404
from django.db import transaction
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from .tasks.callback import process_dedup_request
from .models import LSHIndex
from .serializers import DeduplicationRequestSerializer


@api_view(['POST'])
@transaction.atomic
def deduplication(request: Request):
    serializer = DeduplicationRequestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    if not LSHIndex.objects.filter(
        project__original_project_id=serializer.validated_data["project_id"],
    ).exists():
        raise Http404

    req_obj = serializer.save()
    process_dedup_request.delay(req_obj.pk)
    return Response(
        {
            "message": "Deduplication request has been successfully queued",
        },
        status=status.HTTP_201_CREATED,
    )
