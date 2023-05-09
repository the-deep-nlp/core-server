from unittest.mock import patch
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
    VALID_DATA = {
        "client_id": "1",
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

    def test_tags_mapping_valid_data(self):
        """Pop each item from valid data and check if it gives 400"""
        data = {"items": [self.VALID_DATA]}
        self.set_credentials()
        resp = self.client.post(self.TAGS_MAPPING_URL, data=data, format="json")
        assert resp.status_code == 200
        resp_data = resp.json()
        assert len(resp_data) > 0, "There must be a result"
        for item in resp_data:
            assert "client_id" in item
            assert "input_text" in item
            assert "output_text" in item
            assert "output_tagids" in item
