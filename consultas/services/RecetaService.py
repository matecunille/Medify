from consultas.repositories import RecetaRepository

class RecetaService:
    @staticmethod
    def listar_recetas():
        return RecetaRepository.obtener_todas()

    @staticmethod
    def obtener_receta_por_id(pk):
        return RecetaRepository.obtener_por_id(pk)

    @staticmethod
    def crear_receta(consulta, documento):
        return RecetaRepository.crear(consulta, documento)

    @staticmethod
    def eliminar_receta(pk):
        RecetaRepository.eliminar(pk)

    @staticmethod
    def actualizar_receta(pk, **kwargs):
        RecetaRepository.actualizar(pk, **kwargs)

    @staticmethod
    def listar_recetas_por_consulta(consulta_id):
        return RecetaRepository.obtener_por_consulta(consulta_id)