from typing import List
from unittest.mock import patch
from rest_framework.test import APITestCase, APIClient


from core.models import ToFetchProject, Project
from deduplication.models import LSHIndex, DeduplicationRequest


class TestAPIs(APITestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = APIClient()

    def test_post_dedup_request_invalid_params(self):
        url = "/api/v1/deduplication/"
        full_data = {
            "lead_id": 10,
            "client_id": "client_id",
            "project_id": 1,
            "text_extract": "extract",
            "callback_url": "/https://someurl.com",
        }

        def select(keys: List[str]):
            return {k: full_data[k] for k in keys}

        # The following invalid data consists of different combinations of full data
        # with missing one or two parameters
        invalid_data = [
            select([]),
            select(["lead_id", "project_id", "callback_url", "text_extract"]),
            select(["text_extract", "project_id", "callback_url", "client_id"]),
            select(["text_extract", "lead_id", "callback_url"]),
            select(["text_extract", "project_id", "lead_id"]),
        ]
        for data in invalid_data:
            response = self.client.post(url, data)
            assert response.status_code == 400, f"Should fail for {data}"
            resp_data = response.json()
            assert "message" in resp_data

    @patch("deduplication.views.process_dedup_request")
    def test_post_dedup_request_inexistent_project(self, process_dedup_request):
        """Even if the project does not exist, the request should pass and corresponding
        project and lsh index should be created
        """
        original_prj_id = 100
        original_lead_id = 20
        assert not ToFetchProject.objects.filter(
            original_project_id=original_prj_id
        ).exists()
        data = {
            "lead_id": original_lead_id,
            "client_id": "some_client_id",
            "project_id": original_prj_id,
            "text_extract": "some extract",
            "callback_url": "some url",
        }

        url = "/api/v1/deduplication/"
        response = self.client.post(url, data)
        assert response.status_code == 202
        resp_data = response.json()
        assert "message" in resp_data

        # Assert there is a ToFetchProject object with the project id: either created
        # newly or already existing
        to_fetch_proj = ToFetchProject.objects.filter(
            original_project_id=original_prj_id
        )
        assert to_fetch_proj.exists(), "To fetch project must exist or created"

        # Assert a background function is not called because project leads have
        # not been indexed yet
        dedup_obj = DeduplicationRequest.objects.filter(
            lead_id=original_lead_id,
            project_id=original_prj_id,
        ).first()
        assert dedup_obj is not None, "Deduplication request should be created"
        process_dedup_request.delay.assert_not_called()

    @patch("deduplication.views.process_dedup_request")
    def test_post_dedup_request_project_leads_fetched_index_creating(
        self, process_dedup_request
    ):
        """
        Although leads have been fetched, if index is being created, do not
        call process_dedup_request.
        """
        # First create project
        original_project_id = 10
        original_lead_id = 10
        self.prepare_data_and_test_api_call(
            original_project_id,
            original_lead_id,
            fetch_status=ToFetchProject.FetchStatus.FETCHED,
            index_status=LSHIndex.IndexStatus.CREATING,
        )

        # Assert a background function is called
        dedup_obj = DeduplicationRequest.objects.filter(
            lead_id=original_lead_id,
            project_id=original_project_id,
        ).first()
        assert dedup_obj is not None, "Deduplication request should be created"
        process_dedup_request.delay.assert_not_called()

    @patch("deduplication.views.process_dedup_request")
    def test_post_dedup_request_project_leads_fetched_index_created(
        self, process_dedup_request
    ):
        """
        If index is created, call process_dedup_request right away.
        """
        # First create project
        original_project_id = 10
        original_lead_id = 10
        self.prepare_data_and_test_api_call(
            original_project_id,
            original_lead_id,
            fetch_status=ToFetchProject.FetchStatus.FETCHED,
            index_status=LSHIndex.IndexStatus.CREATED,
        )

        # Assert a background function is called
        dedup_obj = DeduplicationRequest.objects.filter(
            lead_id=original_lead_id,
            project_id=original_project_id,
        ).first()
        assert dedup_obj is not None, "Deduplication request should be created"
        process_dedup_request.delay.assert_called_once_with(dedup_obj.pk)

    @patch("deduplication.views.process_dedup_request")
    def test_post_dedup_request_project_leads_not_fetched(self, process_dedup_request):
        """
        In this case process_dedup request should not be called as leads have
        not all been fetched, let alone indexed
        """
        # First create project
        original_project_id = 10
        original_lead_id = 10
        self.prepare_data_and_test_api_call(
            original_project_id,
            original_lead_id,
            fetch_status=ToFetchProject.FetchStatus.FETCHING,
            index_status=None,
        )

        # Assert a background function is called
        dedup_obj = DeduplicationRequest.objects.filter(
            lead_id=original_lead_id,
            project_id=original_project_id,
        ).first()
        assert dedup_obj is not None, "Deduplication request should be created"
        process_dedup_request.delay.assert_not_called()

    def prepare_data_and_test_api_call(
        self,
        original_project_id,
        original_lead_id,
        fetch_status,
        index_status,
    ):
        to_fetch_proj = ToFetchProject.objects.create(
            original_project_id=original_project_id,
            status=fetch_status,
        )
        prj = Project.objects.create(
            to_fetch_project=to_fetch_proj,
            original_project_id=original_project_id,
            title="Test project",
            location="",
        )
        if index_status is not None:
            # Create an index
            LSHIndex.objects.create(
                name="testindex",
                status=index_status,
                project=prj,
            )
        data = {
            "lead_id": original_lead_id,
            "client_id": "some_client_id",
            "project_id": original_project_id,
            "text_extract": "some extract",
            "callback_url": "some url",
        }
        url = "/api/v1/deduplication/"
        response = self.client.post(url, data)
        assert response.status_code == 202
        resp_data = response.json()
        assert "message" in resp_data
