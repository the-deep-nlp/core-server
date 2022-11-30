from typing import List
from unittest.mock import patch
from rest_framework.test import APITestCase, APIClient


from core.models import Project
from deduplication.models import LSHIndex, DeduplicationRequest


class TestAPIs(APITestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = APIClient()

    def test_post_dedup_request_invalid_params(self):
        url = "/api/deduplication/"
        full_data = {
            "lead_id": 10,
            "project_id": 1,
            "text_extract": "extract",
            "callback_url": "/https://someurl.com",
        }

        def select(keys: List[str]):
            return {k: full_data[k] for k in keys}

        invalid_data = [
            select([]),
            select(['lead_id', 'project_id', 'callback_url']),
            select(['text_extract', 'project_id', 'callback_url']),
            select(['text_extract', 'lead_id', 'callback_url']),
            select(['text_extract', 'project_id', 'lead_id']),
        ]
        for data in invalid_data:
            response = self.client.post(url, data)
            assert response.status_code == 400, f"Should fail for {data}"
            resp_data = response.json()
            assert "message" in resp_data

    @patch('deduplication.views.process_dedup_request')
    def test_post_dedup_request(self, process_dedup_request):
        # First create project
        original_project_id = 10
        original_lead_id = 10
        prj = Project.objects.create(
            original_project_id=original_project_id,
            title="Test project",
            location="",
        )
        # Create an index
        LSHIndex.objects.create(
            name="testindex",
            status=LSHIndex.IndexStatus.CREATED,
            project=prj,
        )
        data = {
            "lead_id": original_lead_id,
            "project_id": original_project_id,
            "text_extract": "some extract",
            "callback_url": "some url",
        }
        url = "/api/deduplication/"
        response = self.client.post(url, data)
        assert response.status_code == 201
        resp_data = response.json()
        assert "message" in resp_data

        # Assert a background function is called
        dedup_obj = DeduplicationRequest.objects.filter(
            lead_id=original_lead_id,
            project_id=original_project_id,
        ).first()
        assert dedup_obj is not None, "Deduplication request should be created"
        process_dedup_request.delay.assert_called_once_with(dedup_obj.pk)

    def test_dedup_non_existent_project_index(self):
        data = {
            "lead_id": 10,
            "project_id": 1000,  # ID 1000 does not exist
            "text_extract": "some extract",
            "callback_url": "some url",
        }
        url = "/api/deduplication/"
        response = self.client.post(url, data)
        assert response.status_code == 404
        resp_data = response.json()
        assert "message" in resp_data
