from django.urls import path, include
from rest_framework.rouetrs import DefaultRouter
from customers.views import CustomerViewSet

router = DefaultRouter()
router.register['customes', CustomerViewSet]

urlpatterns = [
    path('', include(roueter.urls)),
]
