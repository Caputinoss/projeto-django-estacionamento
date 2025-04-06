from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        related_name='customer',
        blank=True,
        null=True,
        verbose_name='Usuário',
    )
    name = models.CharField(
        max_length=50,
        verbose_name='Nome',
    )
    cpf = models.CharField(
        max_length=15,
        verbose_name='CPF',
        blank=True,
        null=True,
    )
    phone = models.CharField(
        max_length=15,
        verbose_name='Telefone',
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
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['name']

    def __str__(self):
        return self.name
