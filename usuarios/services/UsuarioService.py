from usuarios.repositories import UsuarioRepository

class UsuarioService:
    @staticmethod
    def registrar_usuario(username, password, email=None, **extra_fields):
        return UsuarioRepository.crear_usuario(username, password, email, **extra_fields)

    @staticmethod
    def autenticar_usuario(username, password):
        usuario = UsuarioRepository.obtener_por_username(username)
        if usuario and UsuarioRepository.verificar_password(usuario, password):
            return usuario
        return None

    @staticmethod
    def cambiar_contraseña(usuario, nueva_password):
        from django.contrib.auth.hashers import make_password
        usuario.password = make_password(nueva_password)
        usuario.save()

    @staticmethod
    def actualizar_perfil(pk, **kwargs):
        UsuarioRepository.actualizar(pk, **kwargs)

    @staticmethod
    def buscar_por_email(email):
        from usuarios.models import Usuario
        return Usuario.objects.filter(email=email).first()

    @staticmethod
    def verificar_credenciales(username, password):
        usuario = UsuarioRepository.obtener_por_username(username)
        return usuario if usuario and UsuarioRepository.verificar_password(usuario, password) else None