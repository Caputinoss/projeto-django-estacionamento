from rest_framework import viewsets
from parking.serializer import ParkingRecordSerializer, ParkingSpotSerializer
from parking.models import ParkingSpot, ParkingRecord


class ParkingSpotViewSet(viewsets.ModelViewSet):
    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer

class ParkingRecordViewSet(viewsets.ModelViewSet):
    queryset = ParkingRecord.objects.all()
    serializer_class = ParkingRecordSerializer
