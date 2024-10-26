from django.db import models


class Plant(models.Model):
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    watering_frequency_days = models.PositiveIntegerField()
    last_watered_date = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.species}"
