from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions
from parking.serializer import ParkingRecordSerializer, ParkingSpotSerializer
from parking.models import ParkingSpot, ParkingRecord
from core.permissions import IsOwnerOfVehicleOrRecord


class ParkingSpotViewSet(viewsets.ModelViewSet):
    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer
    permission_classes = [DjangoModelPermissions]


class ParkingRecordViewSet(viewsets.ModelViewSet):
    queryset = ParkingRecord.objects.all()
    serializer_class = ParkingRecordSerializer
    permission_classes = [DjangoModelPermissions, IsOwnerOfVehicleOrRecord]

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return ParkingRecord.objects.all()

        return ParkingRecord.objects.filter(vehicle__owner__user=user)
