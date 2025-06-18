from consultas.services.ConsultaService import ConsultaService
from usuarios.repositories import UsuarioRepository
from consultas.models import HORARIOS_CHOICES
from ..repositories.EspecialidadRepository import EspecialidadRepository

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

    @staticmethod
    def obtener_medicos():
        return UsuarioRepository.obtener_todos().filter(rol='medico')

    @staticmethod
    def obtener_pacientes():
        return UsuarioRepository.obtener_todos().filter(rol='paciente')

    @staticmethod
    def obtener_por_id(usuario_id):
        return UsuarioRepository.obtener_por_id(usuario_id)

    @staticmethod
    def obtener_horarios_disponibles(medico_id, fecha_param):
        consultas_ocupadas = ConsultaService.obtener_consultas_por_medico(medico_id=medico_id).filter(fecha=fecha_param)
        horarios_ocupados = [consulta.hora for consulta in consultas_ocupadas]
        turnos_disponibles = [hora for hora, _ in HORARIOS_CHOICES if hora not in horarios_ocupados]
        return turnos_disponibles

    @staticmethod
    def crear_usuario(data):
        # Si es médico, obtener la especialidad
        if data.get('rol') == 'medico' and data.get('especialidad_id'):
            especialidad = EspecialidadRepository.get_by_id(data['especialidad_id'])
            if not especialidad:
                return None
            data['especialidad'] = especialidad
            
        return UsuarioRepository.create_usuario(data)