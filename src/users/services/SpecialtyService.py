from users.repositories.SpecialtyRepository import SpecialtyRepository

class SpecialtyService:
    @staticmethod
    def get_all_specialties():
        return SpecialtyRepository.get_all()
    
    @staticmethod
    def get_active_specialties():
        return SpecialtyRepository.get_active()
    
    @staticmethod
    def get_specialty_by_id(specialty_id):
        return SpecialtyRepository.get_by_id(specialty_id)
    
    @staticmethod
    def create_specialty(name, description=None):
        return SpecialtyRepository.create(name, description)
    
    @staticmethod
    def update_specialty(specialty_id, name=None, description=None, active=None):
        return SpecialtyRepository.update(specialty_id, name, description, active)
    
    @staticmethod
    def delete_specialty(specialty_id):
        return SpecialtyRepository.delete(specialty_id)
    
    @staticmethod
    def deactivate_specialty(specialty_id):
        return SpecialtyRepository.update(specialty_id, active=False)
