from django.contrib import admin
from usuarios.models import Usuario,Paciente,Medico

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