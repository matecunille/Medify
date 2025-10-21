from django.contrib.auth.models import AbstractUser
from django.db import models
from .Specialty import Specialty

class User(AbstractUser):
    ROLE_CHOICES = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    dni = models.CharField(max_length=20, blank=True, null=True)
    specialty = models.ForeignKey(Specialty, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to='users/photos/', blank=True, null=True)
    USERNAME_FIELD = 'username'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"