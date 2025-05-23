from django.contrib import admin
from usuarios.models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'email', 'sexo')
    search_fields = ('nombre', 'email')
    list_filter = ('sexo',)
