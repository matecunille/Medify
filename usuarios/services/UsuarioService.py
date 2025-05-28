from usuarios.repositories import UsuarioRepository

class UsuarioService:

    @staticmethod
    def obtener_todos():
        return UsuarioRepository.obtener_todos()

    @staticmethod
    def crear_usuario(username, email, password, rol):
        from usuarios.models import Usuario
        if UsuarioRepository.obtener_por_username(username):
            return 'usuario_duplicado'
        if UsuarioService.buscar_por_email(email):
            return 'email_duplicado'

        try:
            user = UsuarioRepository.crear_usuario(
                username=username,
                email=email,
                password=password,
                rol=rol
            )
            return user
        except Exception:
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
