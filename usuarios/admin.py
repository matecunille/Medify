from django.contrib import admin
from usuarios.models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'rol']
    list_filter = ['rol']