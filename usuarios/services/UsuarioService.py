from usuarios.repositories import UsuarioRepository

class UsuarioService:

    @staticmethod
    def obtener_todos():
        return UsuarioRepository.obtener_todos()

    @staticmethod
    def crear_usuario(username, email, password, rol, **kwargs):
        try:
            return UsuarioRepository.crear_usuario(
                username=username,
                email=email,
                password=password,
                rol=rol,
                dni=kwargs.get('dni'),
                especialidad=kwargs.get('especialidad') if rol == 'medico' else None,
                first_name=kwargs.get('first_name'),
                last_name=kwargs.get('last_name')
            )
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
    def buscar_por_username(username):
        return UsuarioRepository.obtener_por_username(username)

    @staticmethod
    def buscar_por_email(email):
        from usuarios.models import Usuario
        return Usuario.objects.filter(email=email).first()
