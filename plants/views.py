from rest_framework import viewsets

from plants.models import Plant
from plants.serializers import PlantSerializer, PlantDetailSerializer


class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all()

    def get_serializer_class(self):
        if self.action in ("update", "partial_update"):
            return PlantDetailSerializer
        return PlantSerializer
