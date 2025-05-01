from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Usuario(AbstractUser):
    email = models.EmailField(unique=True)
    sexo = models.IntegerField(choices=[(1, 'Hombre'), (2, 'Mujer'), (3, 'Otro')], default=3)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # Si no querés usar username podés customizar más

    def __str__(self):
        return self.email

class Paciente(Usuario):
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=50)
    documento = models.CharField(max_length=50)

    def __str__(self):
        return self.email

class Medico(Usuario):
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return self.email
