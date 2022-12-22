from rest_framework import serializers

from .models import DeduplicationRequest


class DeduplicationRequestSerializer(serializers.ModelSerializer):
    client_id = serializers.CharField()

    class Meta:
        model = DeduplicationRequest
        exclude = ["error", "result"]
