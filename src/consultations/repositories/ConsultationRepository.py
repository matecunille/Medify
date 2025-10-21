from consultations.models import Consultation

class ConsultationRepository:
    @staticmethod
    def get_by_id(pk):
        return Consultation.objects.filter(pk=pk).first()

    @staticmethod
    def get_all():
        return Consultation.objects.all()

    @staticmethod
    def create(patient, doctor, date, time, description):
        return Consultation.objects.create(
            patient=patient,
            doctor=doctor,
            date=date,
            time=time,
            description=description
        )

    @staticmethod
    def delete(pk):
        Consultation.objects.filter(pk=pk).delete()

    @staticmethod
    def update(pk, **kwargs):
        Consultation.objects.filter(pk=pk).update(**kwargs)

    @staticmethod
    def get_by_doctor_and_date(doctor_id, date):
        return Consultation.objects.filter(
            doctor_id=doctor_id,
            date=date
        )

    @staticmethod
    def get_by_patient(patient_id):
        return Consultation.objects.filter(patient_id=patient_id).order_by('-date', '-time')

    @staticmethod
    def get_by_doctor(doctor_id):
        return Consultation.objects.filter(
            doctor_id=doctor_id
        )