from rest_framework import serializers
from veichles.models import Vehicle, VehicleType

class VehiclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = "__all__"
        read_only_fields = ['id']


class VehiclesTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = "__all__"
        read_only_fields = ['id']