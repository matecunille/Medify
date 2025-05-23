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
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email