from django.db import models
from django.utils import timezone


class Plant(models.Model):
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    watering_frequency_days = models.PositiveIntegerField()
    last_watered_date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f"{self.name} - {self.species}"
