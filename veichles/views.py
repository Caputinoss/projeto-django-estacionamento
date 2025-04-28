from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from veichles.serializer import VehiclesSerializer, VehiclesTypeSerializer
from veichles.models import Vehicle, VehicleType
from core.permissions import IsOwnerOfVehicleOrRecord
from veichles.filters import VehicleFilterClass, VehicleTypeFilterClass


class VehicleTypeViewSet(viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehiclesTypeSerializer
    rql_filter_class = VehicleTypeFilterClass
    permission_classes = [DjangoModelPermissions, IsAdminUser]


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehiclesSerializer
    rql_filter_class = VehicleFilterClass
    
    permission_classes = [DjangoModelPermissions, IsOwnerOfVehicleOrRecord]

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Vehicle.objects.all()

        return Vehicle.objects.filter(owner__user=user)
