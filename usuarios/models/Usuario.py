from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ROL_CHOICES = (
        ('paciente', 'Paciente'),
        ('medico', 'Médico'),
    )
    rol = models.CharField(max_length=10, choices=ROL_CHOICES)
    dni = models.CharField(max_length=20, blank=True, null=True)
    especialidad = models.CharField(max_length=100, blank=True, null=True)
    matricula = models.CharField(max_length=50, blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # Si no querés usar username podés customizar más

    def __str__(self):
        return self.email