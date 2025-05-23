from django.db import models
from .Consulta import Consulta
class Tratamiento(models.Model):
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    medicacion = models.CharField(max_length=255)
    dosis = models.IntegerField (choices = [(1,'5mg'),(2,'10mg'),(3,'25mg'),(4,'50mg'),(5,'100mg'),(6,'200mg')])
    duracion = models.CharField(max_length=100)