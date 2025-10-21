from django.db import models

class Specialty(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Specialty"
        verbose_name_plural = "Specialties"
        ordering = ['name']

    def __str__(self):
        return self.name
