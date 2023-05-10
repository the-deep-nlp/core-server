from copy import deepcopy
from unittest.mock import patch, Mock
from core_server.base_test import BaseTestCase

from core.models import NLPRequest


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
        assert NLPRequest.objects.filter(type="topicmodel").exists()

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
        assert NLPRequest.objects.filter(type="ngrams").exists()

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
        with self.captureOnCommitCallbacks(execute=True):
            self.set_credentials()
            resp = self.client.post(self.SUMMARIZATION_URL, valid_data)
        assert resp.status_code == 202
        spin_ecs_mock.delay.assert_called_once()
        new_requests_count = NLPRequest.objects.count()
        assert \
            new_requests_count == requests_count + 1, \
            "One more NLPRequest object should be created"
        assert NLPRequest.objects.filter(type="summarization").exists()

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
        assert NLPRequest.objects.filter(type="geolocation").exists()


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


class TagsMappingAPI(BaseTestCase):
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
        ).exists(), "NLP request should be created with success status"


class PredictionAPI(BaseTestCase):
    URL = '/api/v1/prediction/'
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
            assert not NLPRequest.objects.filter(client_id=self.CLIENT_ID).exists(), \
                "No nlp request should be created"

    @patch("analysis_module.views.predictions.ModelTagsPrediction")
    def test_prediction_valid_data(self, model_prediction_class):
        self.set_credentials()
        model_prediction_class.return_value.return_value = [{
            "client_id": self.CLIENT_ID,
            "model_preds": [],
        }]
        resp = self.client.post(self.URL, data=self.VALID_DATA, format="json")
        resp_data = resp.json()
        assert resp.status_code == 200
        assert "predictions" in resp_data
        predictions = resp_data["predictions"]
        assert len(predictions) > 0, "There must be a result"
        for item in predictions:
            assert "client_id" in item
            assert "model_preds" in item
        assert NLPRequest.objects.filter(
            client_id=self.CLIENT_ID,
            status=NLPRequest.RequestStatus.SUCCESS,
        ).exists(), "NLP request should be created with success status"

    @patch("analysis_module.views.predictions.ModelTagsPrediction")
    def test_prediction_mock(self, model_prediction_class):
        self.set_credentials()
        data = {**self.VALID_DATA, "mock": True}
        resp = self.client.post(self.URL, data=data, format="json")
        resp_data = resp.json()
        assert "predictions" in resp_data
        predictions = resp_data["predictions"]
        for item in predictions:
            assert "client_id" in item
            assert "model_preds" in item
        assert not NLPRequest.objects.filter(
            client_id=self.CLIENT_ID,
            status=NLPRequest.RequestStatus.SUCCESS,
        ).exists(), "NLP request should not be created for mock request"
        model_prediction_class.assert_not_called()
