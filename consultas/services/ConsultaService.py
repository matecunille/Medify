from consultas.repositories import ConsultaRepository
from consultas.models import ESTADO_CANCELADO

class ConsultaService:
    @staticmethod
    def listar_consultas():
        return ConsultaRepository.obtener_todas()

    @staticmethod
    def obtener_consulta_por_id(pk):
        return ConsultaRepository.obtener_por_id(pk)

    @staticmethod
    def crear_consulta(paciente, medico, fecha, hora, descripcion):
        from usuarios.services import UsuarioService
        medico = UsuarioService.obtener_por_id(medico)
        paciente = UsuarioService.obtener_por_id(paciente)
        return ConsultaRepository.crear(paciente, medico, fecha, hora, descripcion)

    @staticmethod
    def eliminar_consulta(pk):
        ConsultaRepository.eliminar(pk)

    @staticmethod
    def actualizar_consulta(pk, **kwargs):
        ConsultaRepository.actualizar(pk, **kwargs)

    @staticmethod
    def listar_consultas_por_paciente(paciente_id):
        return ConsultaRepository.obtener_por_paciente(paciente_id)

    @staticmethod
    def obtener_consultas_por_medico(medico_id):
        return ConsultaRepository.obtener_por_medico(medico_id)
    
    @staticmethod
    def cancelar_consulta(consulta):
        consulta.estado = ESTADO_CANCELADO
        ConsultaRepository.actualizar(consulta.pk, estado=consulta.estado)
        return