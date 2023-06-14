from django.db import models
from django.contrib.auth.models import AbstractUser
from simple_history.models import HistoricalRecords

from apps.accounts.choices import IDENTIFICATION_CHOICES


class User(AbstractUser):
    type = models.CharField(max_length=2, choices=IDENTIFICATION_CHOICES, null=True)
    document = models.CharField(max_length=255, null=True, unique=True)
    historical = HistoricalRecords()
