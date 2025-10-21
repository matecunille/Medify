from consultations.repositories import ConsultationRepository
from consultations.models import STATUS_CANCELLED

class ConsultationService:
    @staticmethod
    def list_consultations():
        return ConsultationRepository.get_all()

    @staticmethod
    def get_consultation_by_id(pk):
        return ConsultationRepository.get_by_id(pk)

    @staticmethod
    def create_consultation(patient, doctor, date, time, description):
        from users.services import UserService
        doctor = UserService.get_by_id(doctor)
        patient = UserService.get_by_id(patient)
        return ConsultationRepository.create(patient, doctor, date, time, description)

    @staticmethod
    def delete_consultation(pk):
        ConsultationRepository.delete(pk)

    @staticmethod
    def update_consultation(pk, **kwargs):
        ConsultationRepository.update(pk, **kwargs)

    @staticmethod
    def list_consultations_by_patient(patient_id):
        return ConsultationRepository.get_by_patient(patient_id)

    @staticmethod
    def get_consultations_by_doctor(doctor_id):
        return ConsultationRepository.get_by_doctor(doctor_id)
    
    @staticmethod
    def cancel_consultation(consultation):
        consultation.status = STATUS_CANCELLED
        ConsultationRepository.update(consultation.pk, status=consultation.status)
        return
    
    @staticmethod
    def complete_consultation(consultation):
        consultation.status = "completed"
        ConsultationRepository.update(consultation.pk, status=consultation.status)
        return