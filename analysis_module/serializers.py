from django.db import models
from rest_framework import serializers


class BaseEntry(serializers.Serializer):
    entry_id = serializers.CharField()
    excerpt = serializers.CharField()


class BaseAnalysisSerializer(serializers.Serializer):
    client_id = serializers.CharField()
    mock = serializers.BooleanField(default=False)


class GeneralUserSerializer(BaseAnalysisSerializer):
    # not used for now
    entries_url = BaseEntry(many=True)


class EntriesSerializer(BaseAnalysisSerializer):
    entries_url = serializers.URLField()
    callback_url = serializers.CharField(allow_null=True, required=False)


class TopicModelDeepRequest(EntriesSerializer):
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


class NgramsRequest(EntriesSerializer):
    ngrams_config = NgramsParameters()


class StatusRequest(serializers.Serializer):
    unique_id = serializers.UUIDField()


class TagsMappingRequestItem(BaseAnalysisSerializer):
    label = serializers.CharField()
    widget_title = serializers.CharField(allow_null=True)
    parent_label = serializers.CharField(allow_null=True)


class TagsMappingRequestSerializer(serializers.Serializer):
    items = TagsMappingRequestItem(many=True)


class PredictionEntrySerializer(serializers.Serializer):
    client_id = serializers.CharField()
    entry = serializers.CharField()


class PredictionRequestSerializer(serializers.Serializer):
    entries = PredictionEntrySerializer(many=True)
    publishing_organization = serializers.CharField()
    authoring_organization = serializers.ListField()
    callback_url = serializers.CharField()
    mock = serializers.BooleanField(default=False)


class ExtractionDocumentSerializer(serializers.Serializer):
    url = serializers.CharField()
    client_id = serializers.CharField()


class ExtractionRequestTypeChoices(models.IntegerChoices):
    # SYSTEM: Triggered by the client(eg DEEP's) system internally, and this need not
    # be processed right away
    SYSTEM = 0, "SYSTEM"
    # USER: Triggerd by user from the UI, and this needs to be processed right away
    USER = 1, "USER"


class TextExtractionSerializer(serializers.Serializer):
    documents = ExtractionDocumentSerializer(many=True)
    callback_url = serializers.CharField()
    request_type = serializers.ChoiceField(
        choices=ExtractionRequestTypeChoices,
        default=ExtractionRequestTypeChoices.SYSTEM,
    )
    mock = serializers.BooleanField(default=False)


class DocumentURLSerializer(serializers.Serializer):

    url = serializers.URLField()
    client_id = serializers.CharField()


class DocumentTextExtractionIdSerializer(serializers.Serializer):

    text_extraction_id = serializers.CharField()
    client_id = serializers.CharField()


class DocumentEntryExtractionUnionField(serializers.ListField):

    def to_internal_value(self, data):

        data = super().to_internal_value(data)

        result = []
        for item in data:

            url_serializer = DocumentURLSerializer(data=item)
            text_extraction_serializer = DocumentTextExtractionIdSerializer(data=item)

            if url_serializer.is_valid():
                result.append(url_serializer.validated_data)
            elif text_extraction_serializer.is_valid():
                result.append(text_extraction_serializer.validated_data)
            else:
                errors = {}
                errors.update(url_serializer.errors)
                errors.update(text_extraction_serializer.errors)
                raise serializers.ValidationError(errors)

        return result

    def to_representation(self, value):
        return [
            DocumentURLSerializer(item).data if 'url' in item
            else DocumentTextExtractionIdSerializer(item).data
            for item in value
        ]


class EntryExtractionSerializer(serializers.Serializer):

    documents = DocumentEntryExtractionUnionField()
    callback_url = serializers.CharField()
    request_type = serializers.ChoiceField(
        choices=ExtractionRequestTypeChoices,
        default=ExtractionRequestTypeChoices.USER,
    )
    mock = serializers.BooleanField(default=False)
