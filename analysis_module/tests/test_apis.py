from copy import deepcopy
from unittest.mock import patch, Mock
from core_server.base_test import BaseTestCase

from django.test import override_settings
from django.db import transaction

from core.models import NLPRequest
from analysis_module.serializers import ExtractionRequestTypeChoices


class TestAnalysisModuleAPIs(BaseTestCase):
    TOPICMODELING_URL = '/api/v1/topicmodel/'
    NGRAMS_URL = '/api/v1/ngrams/'
    SUMMARIZATION_URL = '/api/v1/summarization/'
    GEOLOCATION_URL = '/api/v1/geolocation/'

    def test_topicmodel_incomplete_data(self):
        """
        This tests for the required params. Each request sent with a missing
        argument should give 400 response.
        """
        valid_data = {
            "entries_url": "https://someurl.com/entries",
            "cluster_size": 2,
            "client_id": "clientid",
            "max_clusters_num": 5,
        }
        params = valid_data.keys()
        for param in params:
            data = dict(valid_data)  # copy original valid data
            data.pop(param)  # This makes it invalid
            self.set_credentials()
            resp = self.client.post(self.TOPICMODELING_URL, data=data)
            assert resp.status_code == 400
            errors = resp.json()["field_errors"]
            assert param in errors

    @patch('analysis_module.views.analysis_module.spin_ecs_container')
    def test_topicmodel_valid_request(self, spin_ecs_mock):
        """
        This tests for a topicmodel api with valid data
        """
        requests_count = NLPRequest.objects.count()
        valid_data = {
            "entries_url": "https://someurl.com/entries",
            "cluster_size": 2,
            "client_id": "someclientid",
            "max_clusters_num": 5,
        }
        with self.captureOnCommitCallbacks(execute=True):
            self.set_credentials()
            resp = self.client.post(self.TOPICMODELING_URL, valid_data)
        assert resp.status_code == 202
        spin_ecs_mock.delay.assert_called_once()
        new_requests_count = NLPRequest.objects.count()
        assert \
            new_requests_count == requests_count + 1, \
            "One more NLPRequest object should be created"
        assert NLPRequest.objects.filter(
            type="topicmodel",
            created_by=self.user,
        ).exists()

    def test_ngrams_incomplete_data(self):
        """
        This tests for the required params. Each request sent with a missing
        argument should give 400 response.
        """
        valid_data = {
            "client_id": "client_id",
            "entries_url": "http://someurl.com/entries",
            "ngrams_config": {
                "generate_unigrams": True,
                "generate_bigrams": True,
                "generate_trigrams": True,
                "enable_stopwords": True,
                "enable_stemming": True,
                "enable_case_sensitive": True,
                "max_ngrams_items": 10,
            },
        }
        params = valid_data.keys()
        for param in params:
            data = dict(valid_data)  # copy original valid data
            data.pop(param)  # This makes it invalid
            self.set_credentials()
            resp = self.client.post(self.NGRAMS_URL, data=data, format="json")
            assert resp.status_code == 400
            errors = resp.json()["field_errors"]
            assert param in errors

    @patch('analysis_module.views.analysis_module.spin_ecs_container')
    def test_ngrams_valid_request(self, spin_ecs_mock):
        requests_count = NLPRequest.objects.count()
        valid_data = {
            "client_id": "client_id",
            "entries_url": "http://someurl.com/entries",
            "ngrams_config": {
                "generate_unigrams": True,
                "enable_case_sensitive": True,
                "max_ngrams_items": 10,
            },
        }
        with self.captureOnCommitCallbacks(execute=True):
            self.set_credentials()
            resp = self.client.post(self.NGRAMS_URL, valid_data, format="json")
        assert resp.status_code == 202
        spin_ecs_mock.delay.assert_called_once()
        new_requests_count = NLPRequest.objects.count()
        assert \
            new_requests_count == requests_count + 1, \
            "One more NLPRequest object should be created"
        assert NLPRequest.objects.filter(
            type="ngrams",
            created_by=self.user,
        ).exists()

    def test_summarization_incomplete_data(self):
        valid_data = {
            "client_id": "client_id",
            "entries_url": "http://someurl.com/entries",
        }
        params = valid_data.keys()
        for param in params:
            data = dict(valid_data)  # copy original valid data
            data.pop(param)  # This makes it invalid
            self.set_credentials()
            resp = self.client.post(self.SUMMARIZATION_URL, data)
            assert resp.status_code == 400
            errors = resp.json()["field_errors"]
            assert param in errors

    @patch('analysis_module.views.analysis_module.spin_ecs_container')
    def test_summarization_valid_request(self, spin_ecs_mock):
        requests_count = NLPRequest.objects.count()
        valid_data = {
            "client_id": "client_id",
            "entries_url": "http://someurl.com/entries",
        }
        with patch("analysis_module.views.analysis_module.USE_NEW_SUMMARIZATION", False), \
                self.captureOnCommitCallbacks(execute=True) as callbacks:
            self.set_credentials()
            resp = self.client.post(self.SUMMARIZATION_URL, valid_data)

        assert len(callbacks) == 1
        assert resp.status_code == 202
        spin_ecs_mock.delay.assert_called_once()
        new_requests_count = NLPRequest.objects.count()
        assert \
            new_requests_count == requests_count + 1, \
            "One more NLPRequest object should be created"
        assert NLPRequest.objects.filter(
            type="summarization",
            created_by=self.user
        ).exists()

    @override_settings(USE_NEW_SUMMARIZATION=True)
    def test_summarization_v2_valid_request(self):
        requests_count = NLPRequest.objects.count()
        valid_data = {
            "client_id": "client_id",
            "entries_url": "http://someurl.com/entries",
        }
        self.set_credentials()
        resp = self.client.post(self.SUMMARIZATION_URL, valid_data)
        assert resp.status_code == 202
        new_requests_count = NLPRequest.objects.count()
        assert \
            new_requests_count == requests_count + 1, \
            "One more NLPRequest object should be created"
        assert NLPRequest.objects.filter(
            type="summarization-v2",
            created_by=self.user,
        ).exists()

    def test_geolocation_incomplete_data(self):
        valid_data = {
            "client_id": "client_id",
            "entries_url": "http://someurl.com/entries",
        }
        params = valid_data.keys()
        for param in params:
            data = dict(valid_data)  # copy original valid data
            data.pop(param)  # This makes it invalid
            self.set_credentials()
            resp = self.client.post(self.GEOLOCATION_URL, data)
            assert resp.status_code == 400
            errors = resp.json()["field_errors"]
            assert param in errors

    @patch('analysis_module.views.analysis_module.spin_ecs_container')
    def test_geolocation_valid_request(self, spin_ecs_mock):
        requests_count = NLPRequest.objects.count()
        valid_data = {
            "client_id": "client_id",
            "entries_url": "http://someurl.com/entries",
        }
        with self.captureOnCommitCallbacks(execute=True):
            self.set_credentials()
            resp = self.client.post(self.GEOLOCATION_URL, valid_data)
        assert resp.status_code == 202
        spin_ecs_mock.delay.assert_called_once()
        new_requests_count = NLPRequest.objects.count()
        assert \
            new_requests_count == requests_count + 1, \
            "One more NLPRequest object should be created"
        assert NLPRequest.objects.filter(
            type="geolocation",
            created_by=self.user
        ).exists()


class TestAnalysisModuleMockAPIs(BaseTestCase):
    TOPICMODELING_URL = '/api/v1/topicmodel/'
    NGRAMS_URL = '/api/v1/ngrams/'
    SUMMARIZATION_URL = '/api/v1/summarization/'
    GEOLOCATION_URL = '/api/v1/geolocation/'
    GET_ENTRIES_DATA = [
        {"entry_id": 1, "excerpt": "Of resolve to gravity thought my prepare chamber so."},
        {"entry_id": 1, "excerpt": "Of resolve to gravity thought my prepare chamber so."},
        {"entry_id": 1, "excerpt": "Of resolve to gravity thought my prepare chamber so."},
        {"entry_id": 1, "excerpt": "Of resolve to gravity thought my prepare chamber so."},
    ]

    @patch('analysis_module.mockserver.process_topicmodeling')
    @patch('analysis_module.mockserver.get_entries_data')
    def test_topicmodel_valid_request(self, get_entries_mock, process_mock):
        """
        This tests for a topicmodel api with valid data
        """
        requests_count = NLPRequest.objects.count()
        valid_data = {
            "client_id": "some client_id",
            "entries_url": "https://someurl.com/entries",
            "cluster_size": 2,
            "max_clusters_num": 5,
            "mock": True,
        }
        get_entries_mock.return_value = self.GET_ENTRIES_DATA
        self.set_credentials()
        resp = self.client.post(self.TOPICMODELING_URL, valid_data)
        assert resp.status_code == 202
        process_mock.delay.assert_called_once()
        new_requests_count = NLPRequest.objects.count()
        assert \
            new_requests_count == requests_count, \
            "No more NLPRequest object should be created"

    @patch('analysis_module.mockserver.process_ngrams')
    @patch('analysis_module.mockserver.get_entries_data')
    def test_ngrams_valid_request(self, get_entries_mock, process_mock):
        requests_count = NLPRequest.objects.count()
        valid_data = {
            "client_id": "client_id",
            "entries_url": "http://someurl.com/entries",
            "callback_url": "http://someurl.com/callback",
            "ngrams_config": {
                "generate_unigrams": True,
                "generate_bigrams": True,
                "generate_trigrams": True,
                "enable_stopwords": True,
                "enable_stemming": True,
                "enable_case_sensitive": True,
                "max_ngrams_items": 10,
            },
            "mock": True,
        }
        get_entries_mock.return_value = self.GET_ENTRIES_DATA
        self.set_credentials()
        resp = self.client.post(self.NGRAMS_URL, valid_data, format="json")
        process_mock.delay.assert_called_once()
        assert resp.status_code == 202
        new_requests_count = NLPRequest.objects.count()
        assert \
            new_requests_count == requests_count, \
            "No more NLPRequest object should be created"

    @patch('analysis_module.mockserver.process_summarization')
    @patch('analysis_module.mockserver.get_entries_data')
    def test_summarization_valid_request(self, get_entries_mock, process_mock):
        requests_count = NLPRequest.objects.count()
        valid_data = {
            "client_id": "client_id",
            "entries_url": "http://someurl.com/entries",
            "callback_url": "http://someurl.com/callback",
            "mock": True,
        }
        get_entries_mock.return_value = self.GET_ENTRIES_DATA
        self.set_credentials()
        resp = self.client.post(self.SUMMARIZATION_URL, valid_data)
        assert resp.status_code == 202
        process_mock.delay.assert_called_once()
        new_requests_count = NLPRequest.objects.count()
        assert \
            new_requests_count == requests_count, \
            "No more NLPRequest object should be created"

    @patch('analysis_module.mockserver.process_geolocation')
    @patch('analysis_module.mockserver.get_entries_data')
    def test_geolocation_valid_request(self, get_entries_mock, process_mock):
        requests_count = NLPRequest.objects.count()
        valid_data = {
            "client_id": "client_id",
            "entries_url": "http://someurl.com/entries",
            "callback_url": "http://someurl.com/callback",
            "mock": True,
        }
        get_entries_mock.return_value = self.GET_ENTRIES_DATA
        self.set_credentials()
        resp = self.client.post(self.GEOLOCATION_URL, valid_data)
        assert resp.status_code == 202
        process_mock.delay.assert_called_once()
        new_requests_count = NLPRequest.objects.count()
        assert \
            new_requests_count == requests_count, \
            "No more NLPRequest object should be created"


class TestTagsMappingAPI(BaseTestCase):
    TAGS_MAPPING_URL = '/api/v1/tags-mapping/'
    CLIENT_ID = "client_id"
    VALID_DATA = {
        "client_id": CLIENT_ID,
        "label": "nutritional status",
        "parent_label": "nutrition",
        "widget_title": None,
    }

    def test_tags_mapping_invalid_data(self):
        """Pop each item from valid data and check if it gives 400"""
        params = self.VALID_DATA.keys()
        for param in params:
            data_ = dict(self.VALID_DATA)
            data_.pop(param)
            data = {"items": [data_]}
            self.set_credentials()
            resp = self.client.post(self.TAGS_MAPPING_URL, data=data, format="json")
            assert resp.status_code == 400

            assert not NLPRequest.objects.filter(client_id=self.CLIENT_ID).exists(), \
                "No nlp request should be created"

    def test_tags_mapping_valid_data(self):
        data = {"items": [self.VALID_DATA]}
        self.set_credentials()
        resp = self.client.post(self.TAGS_MAPPING_URL, data=data, format="json")
        assert resp.status_code == 200
        resp_data = resp.json()
        assert "tags_mapping" in resp_data
        tags_mapping = resp_data["tags_mapping"]
        assert len(tags_mapping) > 0, "There must be a result"
        for item in tags_mapping:
            assert "client_id" in item
            assert "input_text" in item
            assert "output_text" in item
            assert "output_tagids" in item
        assert NLPRequest.objects.filter(
            client_id=self.CLIENT_ID,
            status=NLPRequest.RequestStatus.SUCCESS,
            created_by=self.user,
        ).exists(), "NLP request should be created with success status"


class TestPredictionAPI(BaseTestCase):
    URL = '/api/v1/entry-classification/'
    CLIENT_ID = "client_id"
    VALID_DATA = {
        "entries": [
            {
                "client_id": CLIENT_ID,
                "entry": "this is a sample entry",
            },
        ],
        "publishing_organization": "pub-org",
        "authoring_organization": "auth-org",
        "callback_url": "https://call.me.back/"
    }

    def test_prediction_invalid_data(self):
        params = self.VALID_DATA.keys()
        for param in params:
            data = deepcopy(self.VALID_DATA)
            data.pop(param)
            self.set_credentials()
            resp = self.client.post(self.URL, data=data, format="json")
            assert resp.status_code == 400
            assert param in resp.json()["field_errors"]
            assert not NLPRequest.objects.filter(client_id=self.CLIENT_ID).exists(), \
                "No nlp request should be created"

        # Test invalid entries
        entry_params = ["client_id", "entry"]
        for param in entry_params:
            data = deepcopy(self.VALID_DATA)
            data["entries"][0].pop(param)
            self.set_credentials()
            resp = self.client.post(self.URL, data=data, format="json")
            assert resp.status_code == 400
            assert "entries" in resp.json()["field_errors"]
            assert not NLPRequest.objects.filter(
                client_id=self.CLIENT_ID,
                created_by=self.user,
            ).exists(), \
                "No nlp request should be created"

    # @patch("analysis_module.views.predictions.ModelTagsPrediction")
    # def test_prediction_valid_data(self, model_prediction_class):
    #     self.set_credentials()
    #     model_prediction_class.return_value.return_value = [{
    #         "client_id": self.CLIENT_ID,
    #         "model_preds": [],
    #     }]
    #     resp = self.client.post(self.URL, data=self.VALID_DATA, format="json")
    #     resp_data = resp.json()
    #     assert resp.status_code == 200
    #     assert "classifications" in resp_data
    #     predictions = resp_data["classifications"]
    #     assert len(predictions) > 0, "There must be a result"
    #     for item in predictions:
    #         assert "client_id" in item
    #         assert "model_preds" in item
    #     assert not NLPRequest.objects.filter(
    #         client_id=self.CLIENT_ID,
    #         created_by=self.user,
    #         status=NLPRequest.RequestStatus.SUCCESS,
    #     ).exists(), "No nlp request should be created"

    @patch("analysis_module.views.predictions.ModelTagsPrediction")
    def test_prediction_mock(self, model_prediction_class):
        self.set_credentials()
        data = {**self.VALID_DATA, "mock": True}
        resp = self.client.post(self.URL, data=data, format="json")
        resp_data = resp.json()
        assert "classifications" in resp_data
        predictions = resp_data["classifications"]
        for item in predictions:
            assert "client_id" in item
            assert "model_preds" in item
        assert not NLPRequest.objects.filter(
            client_id=self.CLIENT_ID,
            created_by=self.user,
            status=NLPRequest.RequestStatus.SUCCESS,
        ).exists(), "NLP request should not be created for mock request"
        model_prediction_class.assert_not_called()


class TestTextExtractionAPI(BaseTestCase):
    URL = '/api/v1/text-extraction/'
    CLIENT_ID = "client_id"

    def test_extraction_invalid_data(self):
        no_documents = {"callback_url": "someurl"}
        no_callback_url = {"documents": []}
        no_url = {
            "documents": [{"client_id": "some client id"}],
            "callback_url": "some url"
        }
        no_client_id = {
            "documents": [{"url": "someurl"}],
            "callback_url": "some url"
        }
        request_type_string = {
            "documents": [{"url": "someurl", "client_id": "cid"}],
            "callback_url": "some url",
            "request_type": "somerandom",
        }
        request_type_invalid = {
            "documents": [{"url": "someurl", "client_id": "cid"}],
            "callback_url": "some url",
            "request_type": 20,  # 20 is not a valid request type
        }
        invalid_data = [
            (no_documents, "documents"),
            (no_callback_url, "callback_url"),
            (no_url, "documents"),
            (no_client_id, "documents"),
            (request_type_string, "request_type"),
            (request_type_invalid, "request_type"),
        ]
        for params, err_key in invalid_data:
            self.set_credentials()
            resp = self.client.post(self.URL, data=params)
            assert resp.status_code == 400
            errors = resp.json()["field_errors"]
            assert err_key in errors

    @patch('analysis_module.utils.requests')
    def test_extraction_system_request(self, requests_mock):
        """
        Http request to ECS will not be called right away
        """
        documents = [
            {"url": "someurl", "client_id": self.CLIENT_ID},
            {"url": "anothersomeurl", "client_id": self.CLIENT_ID + "1"},
        ]
        data = {
            "documents": documents,
            "callback_url": "https://call.me.back",
            "request_type": ExtractionRequestTypeChoices.SYSTEM,
        }
        requests_mock.post.return_value = Mock(status_code=200)
        self.set_credentials()
        with self.captureOnCommitCallbacks() as callbacks:
            resp = self.client.post(self.URL, data=data, format="json")

        assert resp.status_code == 202
        assert len(callbacks) == 0

        resp_data = resp.json()
        assert "request_ids" in resp_data
        assert len(resp_data["request_ids"]) == len(documents), "Request ids should be as many as documents"

        req_objects = NLPRequest.objects.filter(
            type=NLPRequest.FeaturesType.TEXT_EXTRACTION,
            created_by=self.user,
            status=NLPRequest.RequestStatus.INITIATED,
        )

        assert req_objects.count() == len(documents), "NLP requests count should be same as the documents count"
        for req_object in req_objects:
            assert req_object.last_process_attempted is None
            assert req_object.process_attempts == 0

    @patch('analysis_module.utils.requests')
    def test_extraction_user_request(self, requests_mock):
        """
        Http request to ECS will be called right away
        """
        documents = [
            {"url": "someurl", "client_id": self.CLIENT_ID},
            {"url": "anothersomeurl", "client_id": self.CLIENT_ID + "1"},
        ]
        data = {
            "documents": documents,
            "callback_url": "https://call.me.back",
            "request_type": ExtractionRequestTypeChoices.USER,
        }
        requests_mock.post.return_value = Mock(status_code=200)
        self.set_credentials()
        with self.captureOnCommitCallbacks() as callbacks:
            resp = self.client.post(self.URL, data=data, format="json")

        assert resp.status_code == 202
        assert len(callbacks) == 2, "There should be one callback for each document"

        for callback in callbacks:
            # Since this does db update, which has to be tested below, need to use on_commit later
            callback()

        resp_data = resp.json()
        assert "request_ids" in resp_data
        assert len(resp_data["request_ids"]) == len(documents), "Request ids should be as many as documents"

        def _test():
            req_objects = NLPRequest.objects.filter(
                type=NLPRequest.FeaturesType.TEXT_EXTRACTION,
                created_by=self.user,
                status=NLPRequest.RequestStatus.INITIATED,
            )

            assert len(req_objects) == len(documents), "NLP requests count should be same as the documents count"
            for req_object in req_objects:
                assert req_object.last_process_attempted is not None, "Attempt must have been made for user request"
                assert req_object.process_attempts == 1, "An attempt must have been made"

        # Because callback() above makes db change
        transaction.on_commit(_test)

    @patch("analysis_module.mockserver.process_extraction_mock.apply_async")
    def test_extraction_mock(self, process_mock):
        data = {
            "documents": [
                {"url": "someurl", "client_id": self.CLIENT_ID},
            ],
            "callback_url": "https://call.me.back",
            "request_type": ExtractionRequestTypeChoices.USER,
            "mock": True,
        }
        self.set_credentials()
        with self.captureOnCommitCallbacks():
            resp = self.client.post(self.URL, data=data, format="json")

        assert resp.status_code == 202

        req_object = NLPRequest.objects.filter(
            type=NLPRequest.FeaturesType.TEXT_EXTRACTION,
            client_id=self.CLIENT_ID,
            created_by=self.user,
            status=NLPRequest.RequestStatus.INITIATED,
        ).first()

        process_mock.assert_called_once()

        assert req_object is None, "NLP request should not be created for mock request"


class TestNLPTags(BaseTestCase):
    URL = "/api/v1/nlp-tags/"

    def test_get_nlp_tags_unauthenticated(self):
        resp = self.client.get(self.URL)
        assert resp.status_code == 401

    def test_get_nlp_tags(self):
        self.set_credentials()
        resp = self.client.get(self.URL)
        assert resp.status_code == 200
        # for tagname, detail in resp.json().items():
        #     assert "label" in detail
        #     assert "group" in detail
        #     assert "is_category" in detail
        #     assert "parent_id" in detail
