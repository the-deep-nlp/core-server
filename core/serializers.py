from rest_framework import serializers

from .models import NLPRequest


class AnalysisModuleRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = NLPRequest
        fields = ["status", "unique_id", "result_s3_link", "type"]
        read_only_fields = ["status", "unique_id", "result_s3_link", "type"]
