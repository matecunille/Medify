from consultations.services.ConsultationService import ConsultationService
from users.repositories import UserRepository
from consultations.models import TIME_SLOTS_CHOICES
from ..repositories.SpecialtyRepository import SpecialtyRepository

class UserService:

    @staticmethod
    def get_all():
        return UserRepository.get_all()

    @staticmethod
    def create_user(username, email, password, role, **kwargs):
        try:
            return UserRepository.create_user(
                username=username,
                email=email,
                password=password,
                role=role,
                dni=kwargs.get('dni'),
                specialty=kwargs.get('specialty') if role == 'doctor' else None,
                first_name=kwargs.get('first_name'),
                last_name=kwargs.get('last_name')
            )
        except Exception:
            return None

    @staticmethod
    def change_password(user, new_password):
        from django.contrib.auth.hashers import make_password
        user.password = make_password(new_password)
        user.save()

    @staticmethod
    def update_profile(pk, **kwargs):
        UserRepository.update(pk, **kwargs)

    @staticmethod
    def find_by_username(username):
        return UserRepository.get_by_username(username)

    @staticmethod
    def find_by_email(email):
        from users.models import User
        return User.objects.filter(email=email).first()

    @staticmethod
    def get_doctors():
        return UserRepository.get_all().filter(role='doctor')

    @staticmethod
    def get_patients():
        return UserRepository.get_all().filter(role='patient')

    @staticmethod
    def get_by_id(user_id):
        return UserRepository.get_by_id(user_id)

    @staticmethod
    def get_available_times(doctor_id, date_param):
        occupied_consultations = ConsultationService.get_consultations_by_doctor(doctor_id=doctor_id).filter(date=date_param)
        occupied_times = [consultation.time for consultation in occupied_consultations]
        available_slots = [time for time, _ in TIME_SLOTS_CHOICES if time not in occupied_times]
        return available_slots

    @staticmethod
    def create_user_data(data):
        # If doctor, get specialty
        if data.get('role') == 'doctor' and data.get('specialty_id'):
            specialty = SpecialtyRepository.get_by_id(data['specialty_id'])
            if not specialty:
                return None
            data['specialty'] = specialty
            
        return UserRepository.create_user(data)