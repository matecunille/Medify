from consultas.repositories import ConsultaRepository

class ConsultaService:
    @staticmethod
    def listar_consultas():
        return ConsultaRepository.obtener_todas()

    @staticmethod
    def obtener_consulta_por_id(pk):
        return ConsultaRepository.obtener_por_id(pk)

    @staticmethod
    def crear_consulta(paciente, medico, fecha, hora, descripcion):
        if ConsultaRepository.obtener_por_medico_y_fecha(medico.id, fecha, hora):
            raise ValueError("El médico ya tiene un turno en ese horario.")
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