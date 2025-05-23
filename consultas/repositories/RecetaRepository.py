from consultas.models import Receta

class RecetaRepository:
    @staticmethod
    def obtener_por_id(pk):
        return Receta.objects.filter(pk=pk).first()

    @staticmethod
    def obtener_todas():
        return Receta.objects.all()

    @staticmethod
    def crear(consulta, documento):
        return Receta.objects.create(
            consulta=consulta,
            documento=documento
        )

    @staticmethod
    def eliminar(pk):
        Receta.objects.filter(pk=pk).delete()

    @staticmethod
    def actualizar(pk, **kwargs):
        Receta.objects.filter(pk=pk).update(**kwargs)

    @staticmethod
    def obtener_por_consulta(consulta_id):
        return Receta.objects.filter(consulta_id=consulta_id)