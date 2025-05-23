from usuarios.models import Usuario
from django.contrib.auth.hashers import make_password, check_password

class UsuarioRepository:
    @staticmethod
    def obtener_por_id(pk):
        return Usuario.objects.filter(pk=pk).first()

    @staticmethod
    def obtener_todos():
        return Usuario.objects.all()

    @staticmethod
    def actualizar(pk, **kwargs):
        Usuario.objects.filter(pk=pk).update(**kwargs)

    @staticmethod
    def eliminar(pk):
        Usuario.objects.filter(pk=pk).delete()

    @staticmethod
    def obtener_por_username(username):
        return Usuario.objects.filter(username=username).first()

    @staticmethod
    def verificar_password(usuario, raw_password):
        return check_password(raw_password, usuario.password)

    @staticmethod
    def crear_usuario(username, password, email=None, **extra_fields):
        hashed_password = make_password(password)
        return Usuario.objects.create(
            username=username,
            password=hashed_password,
            email=email,
            **extra_fields
        )