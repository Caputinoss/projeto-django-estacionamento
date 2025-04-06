from rest_framework import serializers
from parking.models import ParkingRecord, ParkingSpot


class ParkingSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSpot
        fields = "__all__"
        read_only_fields = ['id']


class ParkingRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingRecord
        fields = "__all__"
        read_only_fields = ['id']
