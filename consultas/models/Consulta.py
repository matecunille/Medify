from django.db import models
from usuarios.models import Usuario


class Consulta(models.Model):
    paciente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='consultas_como_paciente')
    medico = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='consultas_como_medico')
    fecha = models.DateField()
    hora = models.TimeField()
    descripcion = models.TextField()