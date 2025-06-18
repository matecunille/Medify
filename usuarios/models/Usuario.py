from django.contrib.auth.models import AbstractUser
from django.db import models
from .Especialidad import Especialidad

class Usuario(AbstractUser):
    ROL_CHOICES = (
        ('paciente', 'Paciente'),
        ('medico', 'Médico'),
    )

    rol = models.CharField(max_length=10, choices=ROL_CHOICES)
    dni = models.CharField(max_length=20, blank=True, null=True)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField(unique=True)
    foto = models.ImageField(upload_to='usuarios/fotos/', blank=True, null=True)
    USERNAME_FIELD = 'username'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"