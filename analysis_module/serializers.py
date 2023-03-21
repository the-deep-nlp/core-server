from rest_framework import serializers


class BaseEntry(serializers.Serializer):

    entry_id = serializers.CharField()
    excerpt = serializers.CharField()


class BaseAnalysisSerializer(serializers.Serializer):

    client_id = serializers.CharField()


class GeneralUserSerializer(BaseAnalysisSerializer):
    # not used for now
    entries_url = BaseEntry(many=True)


class DeepEntriesSerializer(BaseAnalysisSerializer):

    entries_url = serializers.URLField()
    callback_url = serializers.CharField(
        allow_null = True
    )


class TopicModelDeepRequest(DeepEntriesSerializer):
    
    cluster_size = serializers.IntegerField(
        min_value = 1,
        allow_null = True
    )
    max_clusters_num = serializers.IntegerField(
        min_value = 1,
        allow_null = True
    )


class NgramsParameters(serializers.Serializer):
    
    generate_unigrams = serializers.BooleanField(default=True)
    generate_bigrams = serializers.BooleanField(default=True)
    generate_trigrams = serializers.BooleanField(default=True)
    enable_stopwords = serializers.BooleanField(default=True)
    enable_stemming = serializers.BooleanField(default=True)
    enable_case_sensitive = serializers.BooleanField(default=False)
    max_ngrams_items = serializers.IntegerField(default=10)


class NgramsDeepRequest(DeepEntriesSerializer):

    ngrams_config = NgramsParameters()


class StatusRequest(serializers.Serializer):
    unique_id = serializers.UUIDField()