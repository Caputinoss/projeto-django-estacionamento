from django.urls import path, include
from rest_framework.routers import DefaultRouter
from customers.views import CustomerViewSet

app_name = 'customers'

router = DefaultRouter()
router.register('customers', CustomerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
