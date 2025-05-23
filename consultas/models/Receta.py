from django.db import models
from .Consulta import Consulta

class Receta(models.Model):
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE, related_name="recetas_asociadas")
    documento = models.FileField(upload_to='recetas/')