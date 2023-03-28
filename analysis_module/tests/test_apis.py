from unittest.mock import patch
from core_server.base_test import BaseTestCase

from analysis_module.models import AnalysisModuleRequest


class TestAnalysisModuleAPIs(BaseTestCase):
    TOPICMODELING_URL = '/api/v1/topicmodel/'
    NGRAMS_URL = '/api/v1/ngrams/'
    SUMMARIZATION_URL = '/api/v1/summarization/'

    def test_topicmodel_incomplete_data(self):
        """
        This tests for the required params. Each request sent with a missing
        argument should give 400 response.
        """
        valid_data = {
            "client_id": "some client_id",
            "entries_url": "https://someurl.com/entries",
            "cluster_size": 2,
            "callback_url": "https://someurl.com/callback",
            "max_clusters_num": 5,
        }
        params = valid_data.keys()
        for param in params:
            data = dict(valid_data)  # copy original valid data
            data.pop(param)  # This makes it invalid
            resp = self.client.post(self.TOPICMODELING_URL, data=data)
            assert resp.status_code == 400
            errors = resp.json()["field_errors"]
            assert param in errors

    @patch('analysis_module.views.spin_ecs_container')
    def test_topicmodel_valid_request(self, spin_ecs_mock):
        """
        This tests for a topicmodel api with valid data
        """
        requests_count = AnalysisModuleRequest.objects.count()
        valid_data = {
            "client_id": "some client_id",
            "entries_url": "https://someurl.com/entries",
            "cluster_size": 2,
            "callback_url": "https://someurl.com/callback",
            "max_clusters_num": 5,
        }
        resp = self.client.post(self.TOPICMODELING_URL, valid_data)
        spin_ecs_mock.assert_called_once()
        assert resp.status_code == 202
        new_requests_count = AnalysisModuleRequest.objects.count()
        assert \
            new_requests_count == requests_count + 1, \
            "One more AnalysisModuleRequest object should be created"
        assert AnalysisModuleRequest.objects.filter(type="topicmodel").exists()

    def test_ngrams_incomplete_data(self):
        """
        This tests for the required params. Each request sent with a missing
        argument should give 400 response.
        """
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
        }
        params = valid_data.keys()
        for param in params:
            data = dict(valid_data)  # copy original valid data
            data.pop(param)  # This makes it invalid
            resp = self.client.post(self.NGRAMS_URL, data=data, format="json")
            assert resp.status_code == 400
            errors = resp.json()["field_errors"]
            assert param in errors

    @patch('analysis_module.views.spin_ecs_container')
    def test_ngrams_valid_request(self, spin_ecs_mock):
        requests_count = AnalysisModuleRequest.objects.count()
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
        }
        resp = self.client.post(self.NGRAMS_URL, valid_data, format="json")
        spin_ecs_mock.assert_called_once()
        assert resp.status_code == 202
        new_requests_count = AnalysisModuleRequest.objects.count()
        assert \
            new_requests_count == requests_count + 1, \
            "One more AnalysisModuleRequest object should be created"
        assert AnalysisModuleRequest.objects.filter(type="ngrams").exists()

    def test_summarization_incomplete_data(self):
        valid_data = {
            "client_id": "client_id",
            "entries_url": "http://someurl.com/entries",
            "callback_url": "http://someurl.com/callback",
        }
        params = valid_data.keys()
        for param in params:
            data = dict(valid_data)  # copy original valid data
            data.pop(param)  # This makes it invalid
            resp = self.client.post(self.SUMMARIZATION_URL, data)
            assert resp.status_code == 400
            errors = resp.json()["field_errors"]
            assert param in errors

    @patch('analysis_module.views.spin_ecs_container')
    def test_summarization_valid_request(self, spin_ecs_mock):
        requests_count = AnalysisModuleRequest.objects.count()
        valid_data = {
            "client_id": "client_id",
            "entries_url": "http://someurl.com/entries",
            "callback_url": "http://someurl.com/callback",
        }
        resp = self.client.post(self.SUMMARIZATION_URL, valid_data)
        spin_ecs_mock.assert_called_once()
        assert resp.status_code == 202
        new_requests_count = AnalysisModuleRequest.objects.count()
        assert \
            new_requests_count == requests_count + 1, \
            "One more AnalysisModuleRequest object should be created"
        assert AnalysisModuleRequest.objects.filter(type="summarization").exists()


class TestAnalysisModuleMockAPIs(BaseTestCase):
    TOPICMODELING_URL = '/api/v1/topicmodel/'
    NGRAMS_URL = '/api/v1/ngrams/'
    SUMMARIZATION_URL = '/api/v1/summarization/'

    @patch('analysis_module.views.spin_ecs_container')
    def test_topicmodel_valid_request(self, spin_ecs_mock):
        """
        This tests for a topicmodel api with valid data
        """
        requests_count = AnalysisModuleRequest.objects.count()
        valid_data = {
            "client_id": "some client_id",
            "entries_url": "https://someurl.com/entries",
            "cluster_size": 2,
            "callback_url": "https://someurl.com/callback",
            "max_clusters_num": 5,
            "mock": True,
        }
        resp = self.client.post(self.TOPICMODELING_URL, valid_data)
        spin_ecs_mock.assert_called_once()
        assert resp.status_code == 202
        new_requests_count = AnalysisModuleRequest.objects.count()
        assert \
            new_requests_count == requests_count + 1, \
            "One more AnalysisModuleRequest object should be created"
        assert AnalysisModuleRequest.objects.filter(type="topicmodel").exists()

    @patch('analysis_module.views.spin_ecs_container')
    def test_ngrams_valid_request(self, spin_ecs_mock):
        requests_count = AnalysisModuleRequest.objects.count()
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
        resp = self.client.post(self.NGRAMS_URL, valid_data, format="json")
        spin_ecs_mock.assert_called_once()
        assert resp.status_code == 202
        new_requests_count = AnalysisModuleRequest.objects.count()
        assert \
            new_requests_count == requests_count + 1, \
            "One more AnalysisModuleRequest object should be created"
        assert AnalysisModuleRequest.objects.filter(type="ngrams").exists()

    @patch('analysis_module.views.spin_ecs_container')
    def test_summarization_valid_request(self, spin_ecs_mock):
        requests_count = AnalysisModuleRequest.objects.count()
        valid_data = {
            "client_id": "client_id",
            "entries_url": "http://someurl.com/entries",
            "callback_url": "http://someurl.com/callback",
            "mock": True,
        }
        resp = self.client.post(self.SUMMARIZATION_URL, valid_data)
        spin_ecs_mock.assert_called_once()
        assert resp.status_code == 202
        new_requests_count = AnalysisModuleRequest.objects.count()
        assert \
            new_requests_count == requests_count + 1, \
            "One more AnalysisModuleRequest object should be created"
        assert AnalysisModuleRequest.objects.filter(type="summarization").exists()
