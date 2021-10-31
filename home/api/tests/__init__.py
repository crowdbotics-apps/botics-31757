import factory
from django.utils import timezone
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIClient

from home.models import App


User = get_user_model()


class AppFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = App


class BaseAPITestCase(APITestCase):

    def setUp(self):
        self.user_admin = User.objects.create_superuser(
            username='test_admin',
            email='test_admin@gmail.com',
            password='password123',
        )

        AppFactory(
            name="test app-2",
            description="Backend API",
            type="Web",
            framework="Django",
            domain_name="testapp-2",
            user=self.user_admin
        )

        self.client = APIClient()
        self.client.login(username='test_admin', password='password123')
