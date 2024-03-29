from core_server.base_test import BaseTestCase


class TestApiAuth(BaseTestCase):
    URL = '/api/v1/test-auth/'

    def test_auth_no_auth_token(self):
        resp = self.client.post(self.URL)
        assert resp.status_code == 401

    def test_auth_with_auth_token(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        resp = self.client.post(self.URL)
        assert resp.status_code == 200
