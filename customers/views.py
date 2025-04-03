from rest_framework import viewsets
from customers.serializer import CustomerSerializer
from customers.models import Customer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
