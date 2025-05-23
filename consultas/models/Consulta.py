from django.db import models
from usuarios.models import Usuario


class Consulta(models.Model):
    paciente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    medico = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    descripcion = models.TextField()