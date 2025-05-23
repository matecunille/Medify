from consultas.models import Tratamiento

class TratamientoRepository:
    @staticmethod
    def obtener_por_id(pk):
        return Tratamiento.objects.filter(pk=pk).first()

    @staticmethod
    def obtener_todos():
        return Tratamiento.objects.all()

    @staticmethod
    def crear(consulta, medicacion, dosis, duracion):
        return Tratamiento.objects.create(
            consulta=consulta,
            medicacion=medicacion,
            dosis=dosis,
            duracion=duracion
        )

    @staticmethod
    def eliminar(pk):
        Tratamiento.objects.filter(pk=pk).delete()

    @staticmethod
    def actualizar(pk, **kwargs):
        Tratamiento.objects.filter(pk=pk).update(**kwargs)

    @staticmethod
    def obtener_por_consulta(consulta_id):
        return Tratamiento.objects.filter(consulta_id=consulta_id)