from enum import Enum
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class AppType(Enum):
    WEB = 'Web'
    MOBILE = 'Mobile'


class AppFramework(Enum):
    DJANGO = 'Django'
    REACT_NATIVE = 'React Native'


# class BaseModel(models.Model):
    


class Plan(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    app = models.ForeignKey('home.App', on_delete=models.CASCADE, related_name='subscription_app')
    plan = models.ForeignKey('home.Plan', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class App(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(null=True, blank=True, max_length=255)
    type = models.CharField(max_length=10, choices=[(tag, tag.value) for tag in AppType])
    framework = models.CharField(max_length=10, choices=[(tag, tag.value) for tag in AppFramework])
    domain_name = models.CharField(max_length=50, blank=True, null=True)
    screenshot = models.URLField(blank=True, null=True)
    subscription = models.ForeignKey('home.Subscription', blank=True, null=True, on_delete=models.SET_NULL, related_name='app_subscription')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
