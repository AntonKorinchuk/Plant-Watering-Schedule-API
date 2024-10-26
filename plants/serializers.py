from rest_framework import serializers

from plants.models import Plant


class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ("id", "name", "species", "watering_frequency_days", "last_watered_days",)
        read_only_fields = ("id", "name", "species", "watering_frequency_days",)
