from django.contrib import admin

from consultas.models import Consulta


# Register your models here.
@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'hora', 'paciente', 'medico','estado')
    list_filter = ('fecha',)
