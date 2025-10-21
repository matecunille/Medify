from django.contrib import admin

from consultations.models import Consultation


# Register your models here.
@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'time', 'patient', 'doctor', 'status')
    list_filter = ('date',)
