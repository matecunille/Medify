from consultas.models import Consulta

class ConsultaRepository:
    @staticmethod
    def obtener_por_id(pk):
        return Consulta.objects.filter(pk=pk).first()

    @staticmethod
    def obtener_todas():
        return Consulta.objects.all()

    @staticmethod
    def crear(paciente, medico, fecha, hora, descripcion):
        return Consulta.objects.create(
            paciente=paciente,
            medico=medico,
            fecha=fecha,
            hora=hora,
            descripcion=descripcion
        )

    @staticmethod
    def eliminar(pk):
        Consulta.objects.filter(pk=pk).delete()

    @staticmethod
    def actualizar(pk, **kwargs):
        Consulta.objects.filter(pk=pk).update(**kwargs)

    @staticmethod
    def obtener_por_medico_y_fecha(medico_id, fecha):
        return Consulta.objects.filter(
            medico_id=medico_id,
            fecha=fecha
        )

    @staticmethod
    def obtener_por_paciente(paciente_id):
        return Consulta.objects.filter(paciente_id=paciente_id).order_by('-fecha', '-hora')

    @staticmethod
    def obtener_por_medico(medico_id):
        return Consulta.objects.filter(
            medico_id=medico_id
        )