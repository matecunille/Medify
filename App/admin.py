from django.contrib import admin
from .models import Usuario, Paciente, Medico, Consulta, Tratamiento, Receta

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'email', 'sexo')
    search_fields = ('nombre', 'email')
    list_filter = ('sexo',)

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'documento')
    search_fields = ('usuario__nombre', 'documento')

@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'especialidad')
    search_fields = ('usuario__nombre', 'especialidad')

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'hora', 'paciente', 'medico')
    list_filter = ('fecha',)

admin.site.register(Tratamiento)
admin.site.register(Receta)