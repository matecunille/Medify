from django.db import models
from django.conf import settings

HORARIOS_CHOICES = [
    ('09:00', '09:00'),
    ('10:00', '10:00'),
    ('11:00', '11:00'),
    ('12:00', '12:00'),
    ('13:00', '13:00'),
    ('14:00', '14:00'),
    ('15:00', '15:00'),
    ('16:00', '16:00'),
]

ESTADO_CANCELADO = 'cancelada'

ESTADOS_CHOICES = [
    ('pendiente', 'Pendiente'),
    ('concluida', 'Concluida'),
    (ESTADO_CANCELADO, 'Cancelada'),
]

class Consulta(models.Model):
    fecha = models.DateField()
    estado = models.CharField(max_length=10, choices=ESTADOS_CHOICES, default='pendiente')
    hora = models.CharField(max_length=5, choices=HORARIOS_CHOICES)
    descripcion = models.TextField()
    paciente = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='consultas_como_paciente'
    )
    medico = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='consultas_como_medico'
    )

    def __str__(self):
        return f'{self.fecha} {self.hora} - {self.paciente} con {self.medico}'