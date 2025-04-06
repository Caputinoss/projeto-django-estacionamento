from django.db import models
from customers.models import Customer


class VehicleType(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Nome',
        unique=True,
    )
    description = models.TextField(
        verbose_name='Descrição',
        blank=True,
        null=True,
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
        verbose_name = 'Tipo de Veículo'
        verbose_name_plural = 'Tipos de Veículos'
        ordering = ['name']

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(
        VehicleType,
        on_delete=models.PROTECT,
        related_name='vehicles',
        verbose_name='Tipo de Veículo',
        blank=True,
        null=True,
    )
    license_plate = models.CharField(
        max_length=10,
        verbose_name='Placa',
        unique=True,
    )
    brand = models.CharField(
        max_length=50,
        verbose_name='Marca',
        blank=True,
        null=True,
    )
    model = models.CharField(
        max_length=50,
        verbose_name='Modelo',
        blank=True,
        null=True,
    )
    color = models.CharField(
        max_length=20,
        verbose_name='Cor',
        blank=True,
        null=True,
    )
    owner = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        related_name='vehicles',
        verbose_name='Proprietário',
        blank=True,
        null=True,
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
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'
        ordering = ['license_plate']

    def __str__(self):
        return self.license_plate
