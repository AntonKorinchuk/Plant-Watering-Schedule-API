from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.utils import timezone

from plants.models import Plant


class PlantTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.plant = Plant.objects.create(
            name="Plant",
            species="Species",
            watering_frequency_days=2,
            last_watered_date=timezone.now(),
        )

    def test_update_last_watered_date(self):
        url = reverse("plants:plant-detail", args=[self.plant.id])
        new_date = timezone.now()
        response = self.client.patch(
            url, {"last_watered_date": new_date}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.plant.refresh_from_db()
        self.assertEqual(self.plant.last_watered_date, new_date)

    def test_mark_as_watered(self):
        url = reverse("plants:plant-mark-as-watered", args=[self.plant.id])
        response = self.client.post(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.plant.refresh_from_db()
        self.assertEqual(self.plant.last_watered_date.date(), timezone.now().date())
