from django.db import models
from simple_history.models import HistoricalRecords


class ExceptionLog(models.Model):
    name = models.CharField(max_length=255, null=True, help_text="Name of the class, method, or function of the error")
    path = models.CharField(max_length=255, null=True, help_text="The path where the error is in the app")
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    history = HistoricalRecords()

    def __str__(self):
        return f"{self.message}"
