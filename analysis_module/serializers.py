from rest_framework import serializers

from .models import AnalysisModuleRequest


class BaseEntry(serializers.Serializer):
    entry_id = serializers.CharField()
    excerpt = serializers.CharField()


class BaseAnalysisSerializer(serializers.Serializer):
    client_id = serializers.CharField()
    mock = serializers.BooleanField(default=False)


class GeneralUserSerializer(BaseAnalysisSerializer):
    # not used for now
    entries_url = BaseEntry(many=True)


class DeepEntriesSerializer(BaseAnalysisSerializer):
    entries_url = serializers.URLField()
    callback_url = serializers.CharField(allow_null=True, required=False)


class TopicModelDeepRequest(DeepEntriesSerializer):
    cluster_size = serializers.IntegerField(min_value=1, allow_null=True)
    max_clusters_num = serializers.IntegerField(min_value=1, allow_null=True)


class NgramsParameters(serializers.Serializer):
    generate_unigrams = serializers.BooleanField(default=True, required=False)
    generate_bigrams = serializers.BooleanField(default=True, required=False)
    generate_trigrams = serializers.BooleanField(default=True, required=False)
    enable_stopwords = serializers.BooleanField(default=True, required=False)
    enable_stemming = serializers.BooleanField(default=False, required=False)
    enable_end_of_sentence = serializers.BooleanField(default=True, required=False)
    enable_case_sensitive = serializers.BooleanField(default=False, required=False)
    max_ngrams_items = serializers.IntegerField(default=10, required=False)


class NgramsDeepRequest(DeepEntriesSerializer):
    ngrams_config = NgramsParameters()


class StatusRequest(serializers.Serializer):
    unique_id = serializers.UUIDField()


class AnalysisModuleRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalysisModuleRequest
        fields = ["status", "unique_id", "result_s3_link", "type"]
        read_only_fields = ["status", "unique_id", "result_s3_link", "type"]
