from consultas.repositories import TratamientoRepository

class TratamientoService:
    @staticmethod
    def listar_tratamientos():
        return TratamientoRepository.obtener_todos()

    @staticmethod
    def obtener_tratamiento_por_id(pk):
        return TratamientoRepository.obtener_por_id(pk)

    @staticmethod
    def crear_tratamiento(consulta, medicacion, dosis, duracion):
        return TratamientoRepository.crear(consulta, medicacion, dosis, duracion)

    @staticmethod
    def eliminar_tratamiento(pk):
        TratamientoRepository.eliminar(pk)

    @staticmethod
    def actualizar_tratamiento(pk, **kwargs):
        TratamientoRepository.actualizar(pk, **kwargs)

    @staticmethod
    def listar_tratamientos_por_consulta(consulta_id):
        return TratamientoRepository.obtener_por_consulta(consulta_id)