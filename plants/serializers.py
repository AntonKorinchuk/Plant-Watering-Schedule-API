from rest_framework import serializers

from plants.models import Plant


class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = (
            "id",
            "name",
            "species",
            "watering_frequency_days",
            "last_watered_date",
        )
        extra_kwargs = {
            "name": {"required": True},
            "species": {"required": True},
            "watering_frequency_days": {"required": True},
            "last_watered_date": {"required": False},
        }


class PlantDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = (
            "id",
            "name",
            "species",
            "watering_frequency_days",
            "last_watered_date",
        )
        read_only_fields = ("id", "name", "species", "watering_frequency_days")
