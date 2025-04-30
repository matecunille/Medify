from random import choices

from django.contrib.auth.models import AbstractUser
from django.db import models


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

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    descripcion = models.TextField()

class Tratamiento(models.Model):
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    medicacion = models.CharField(max_length=255)
    dosis = models.IntegerField (choices = [(1,'5mg'),(2,'10mg'),(3,'25mg'),(4,'50mg'),(5,'100mg'),(6,'200mg')])
    duracion = models.CharField(max_length=100)

class Receta(models.Model):
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    documento = models.FileField(upload_to='recetas/')