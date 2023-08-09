from datetime import datetime, timedelta
from unittest.mock import patch, Mock

from core_server.base_test import BaseTestCase

from core.models import FailedCallback, NLPRequest
from core.tasks.callbacks import get_failed_callbacks


class TestFailedCallback(BaseTestCase):
    def setUp(self):
        super().setUp()

    def create_failed_callback(self, status=FailedCallback.Status.RETRYING, **kwargs):
        req = NLPRequest.objects.create(
            client_id="some_client_id",
            request_params={"callback_url": "http://someurl.py"},
            type="ngrams",  # this is arbitrary choice
        )
        return FailedCallback.objects.create(
            status=status,
            request_unique_id=req.unique_id,
            **kwargs,
        )

    @patch("core.models.requests.post")
    def test_resend_callback_request_successful(self, requests_patch):
        failed_callback = self.create_failed_callback()
        requests_patch.return_value = Mock(status_code=201)
        failed_callback.resend_callback_request()
        requests_patch.assert_called_once()
        failed_callback.refresh_from_db()
        assert failed_callback.status == FailedCallback.Status.SUCCESS

    @patch("core.models.requests.post")
    def test_resend_callback_request_no_callback_url(self, requests_patch):
        # Create a request without callback in params
        req = NLPRequest.objects.create(
            client_id="some_client_id",
            request_params={},
            type="ngrams",  # this is arbitrary choice
        )
        failed_callback = FailedCallback.objects.create(
            status=FailedCallback.Status.RETRYING,
            request_unique_id=req.unique_id,
        )
        requests_patch.return_value = Mock(status_code=201)
        failed_callback.resend_callback_request()
        requests_patch.assert_not_called()
        failed_callback.refresh_from_db()
        assert failed_callback.status == FailedCallback.Status.FAILED

    def test_get_failed_callbacks(self):
        now = datetime.now()
        old_callback = self.create_failed_callback(
            status=FailedCallback.Status.RETRYING,
        )
        old_callback.created_at = now - timedelta(hours=266)
        old_callback.save()
        # Callback within a day
        new_callback = self.create_failed_callback(
            created_at=now - timedelta(hours=20),
            status=FailedCallback.Status.RETRYING,
        )
        failed_callbacks = get_failed_callbacks()
        assert len(failed_callbacks) == 1, "Only one callback should be present"
        assert failed_callbacks[0].id == new_callback.id
