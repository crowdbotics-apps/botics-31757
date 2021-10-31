import factory
from django.utils import timezone
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIClient

from home.models import App, Plan, Subscription


User = get_user_model()


class AppFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = App


class PlanFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Plan


class SubscriptionFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Subscription


class BaseAPITestCase(APITestCase):

    def setUp(self):
        self.user_admin = User.objects.create_superuser(
            username='test_admin',
            email='test_admin@gmail.com',
            password='password123',
        )

        self.app1 = AppFactory(
            name="test app-2",
            description="Backend API",
            type="Web",
            framework="Django",
            domain_name="testapp-2",
            user=self.user_admin
        )

        self.app2 = AppFactory(
            name="meta",
            description="Backend API",
            type="Web",
            framework="Django",
            domain_name="meta",
            user=self.user_admin
        )

        self.plan1 = PlanFactory(
            name="Pro",
            description="pro-tier",
            price=25.00
        )

        self.plan2 = PlanFactory(
            name="Free",
            description="free-tier",
            price=0.00
        )

        self.plan3 = PlanFactory(
            name="Standard",
            description="standard-tier",
            price=10.00
        )

        self.sub1 = SubscriptionFactory(
            plan=self.plan1,
            app=self.app1,
            active=True,
            user=self.user_admin
        )

        self.client = APIClient()
        self.client.login(username='test_admin', password='password123')
