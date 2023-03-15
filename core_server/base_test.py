from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient  # type: ignore


class BaseTestCase(APITestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = APIClient()

    def setUp(self):
        super().setUp()
        self.user = User.objects.create(
            first_name="Test",
            last_name="User",
            email="testuser@deepl.org",
        )
