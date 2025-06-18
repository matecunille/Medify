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
    def crear_usuario(data):
        try:
            # Primero creamos el usuario sin la especialidad
            hashed_password = make_password(data['password'])
            usuario = Usuario.objects.create(
                username=data['username'],
                password=hashed_password,
                email=data['email'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                rol=data['rol'],
                dni=data['dni'],
                foto=data.get('foto')
            )
            
            # Si es médico y tiene especialidad, la asignamos
            if data['rol'] == 'medico' and 'especialidad' in data:
                usuario.especialidad = data['especialidad']
                usuario.save()
                
            return usuario
        except Exception as e:
            print(f"Error al crear usuario: {e}")
            return None