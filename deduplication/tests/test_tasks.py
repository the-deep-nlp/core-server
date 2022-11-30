import pytest
from unittest import TestCase
from unittest.mock import patch

from core.models import Project
from deduplication.models import DeduplicationRequest, LSHIndex
from deduplication.tasks.callback import process_dedup_request


@pytest.mark.django_db
class TestTasks(TestCase):
    """
    Unit tests for the tasks in deduplication module
    """
    @patch('deduplication.tasks.callback.get_minhash')
    def test_process_dedup_request_inexistent_request(self, minhash_func):
        inexistent_pk = 1000
        process_dedup_request(inexistent_pk)
        minhash_func.assert_not_called()

    @patch('deduplication.tasks.callback.respond_to_deep')
    @patch('deduplication.tasks.callback.get_minhash')
    def test_process_dedup_request_invalid_dedup_request(self, minhash_func, respond_to_deep):
        """
        The dedup request exists but corresponding LSHIndex does not exist
        """
        deep_callback_url = "http://callback-url.thedeep.io"  # This is dummy
        dedup_req = DeduplicationRequest.objects.create(
            project_id=1,  # dummy id, corresponding lsh index does not exist
            lead_id=1,  # dummy
            callback_url=deep_callback_url,
        )
        process_dedup_request(dedup_req.pk)
        minhash_func.assert_not_called()
        respond_to_deep.assert_not_called()

    @patch('deduplication.tasks.callback.respond_to_deep')
    def test_process_dedup_request_valid_dedup_request(self, respond_to_deep):
        deep_callback_url = "http://callback-url.thedeep.io"  # This is dummy
        project_id = 1
        project = Project.objects.create(
            original_project_id=project_id,
            title="",
            location="",
        )
        LSHIndex.objects.create(
            name="",
            project=project,
        )
        dedup_req = DeduplicationRequest.objects.create(
            project_id=1,  # dummy id
            lead_id=1,  # dummy
            callback_url=deep_callback_url,

        )
        respond_to_deep.return_value = True, ""
        process_dedup_request(dedup_req.pk)
        respond_to_deep.assert_called_once_with(dedup_req)
