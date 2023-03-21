from core_server.base_test import BaseTestCase
from rest_framework.authtoken.models import Token


class TestApiAuth(BaseTestCase):
    URL = '/api/v1/test-auth/'

    def test_auth_no_auth_token(self):
        resp = self.client.post(self.URL)
        assert resp.status_code == 401

    def test_auth_with_auth_token(self):
        token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        resp = self.client.post(self.URL)
        assert resp.status_code == 200
