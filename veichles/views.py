from rest_framework import viewsets
from veichles.serializer import VehiclesSerializer, VehiclesTypeSerializer
from veichles.models import Vehicle, VehicleType

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehiclesSerializer

class VehicleTypeViewSet(viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehiclesTypeSerializer
