from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from plants.models import Plant
from plants.serializers import PlantSerializer, PlantDetailSerializer


class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all()

    def get_serializer_class(self):
        if self.action in ("update", "partial_update"):
            return PlantDetailSerializer
        return PlantSerializer

    @action(detail=True, methods=["post"])
    def mark_as_watered(self, request, pk=None):
        plant = self.get_object()
        plant.last_watered_date = timezone.now()
        plant.save()
        return Response(
            {
                "status": "plant watered",
                "last_watered_date": plant.last_watered_date
            },
            status=status.HTTP_200_OK
        )
