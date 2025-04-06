from django.urls import path, include
from rest_framework.routers import DefaultRouter
from veichles.views import VehicleTypeViewSet, VehicleViewSet

app_name = 'veichles'

router = DefaultRouter()
router.register('vehicles', VehicleViewSet)
router.register('vehicle_types', VehicleTypeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
