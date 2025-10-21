from django.db import models
from django.conf import settings

TIME_SLOTS_CHOICES = [
    ('09:00', '09:00'),
    ('10:00', '10:00'),
    ('11:00', '11:00'),
    ('12:00', '12:00'),
    ('13:00', '13:00'),
    ('14:00', '14:00'),
    ('15:00', '15:00'),
    ('16:00', '16:00'),
]

STATUS_CANCELLED = 'cancelled'
STATUS_COMPLETED = 'completed'

STATUS_CHOICES = [
    ('pending', 'Pending'),
    (STATUS_COMPLETED, 'Completed'),
    (STATUS_CANCELLED, 'Cancelled'),
]

class Consultation(models.Model):
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    time = models.CharField(max_length=5, choices=TIME_SLOTS_CHOICES)
    description = models.TextField()
    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='consultations_as_patient'
    )
    doctor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='consultations_as_doctor'
    )

    def __str__(self):
        return f'{self.date} {self.time} - {self.patient} with {self.doctor}'