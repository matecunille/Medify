from django.contrib import admin

from consultas.models import Consulta,Receta,Tratamiento


# Register your models here.
@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'hora', 'paciente', 'medico')
    list_filter = ('fecha',)

admin.site.register(Tratamiento)
admin.site.register(Receta)