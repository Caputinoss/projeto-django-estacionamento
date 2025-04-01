from django.db import models
from veichles.models import Vehicle
from customers.models import Customer

# Create your models here.
class ParkingSpot(models.Model):
    spot_number = models.CharField(
        max_length=10, 
        verbose_name='Número da Vaga',
        unique=True,
    )
    is_occupied = models.BooleanField(
        default=False, 
        verbose_name='Ocupada',
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Criado em',
    )
    updated_at = models.DateTimeField(
        auto_now=True, 
        verbose_name='Atualizado em',
    )

    class Meta:
        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'
        ordering = ['spot_number']
    
    def __str__(self):
        return self.spot_number

class ParkingRecord(models.Model):
    vehicle = models.ForeignKey(
        Vehicle, 
        on_delete=models.PROTECT, 
        related_name='parking_records',
        verbose_name='Veículo',
        blank=True,
        null=True,
    )
    parking_spot = models.ForeignKey(
        ParkingSpot, 
        on_delete=models.PROTECT, 
        related_name='parking_records',
        verbose_name='Vaga',
    )
    entry_time = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Entrada',
    )
    exit_time = models.DateTimeField(
        blank=True,
        null=True, 
        verbose_name='Saída',
    )

    class Meta:
        verbose_name = 'Registro de Estacionamento'
        verbose_name_plural = 'Registros de Estacionamento'

    def __str__(self):
        return f'{self.vehicle} - {self.parking_spot} - {self.entry_time}'