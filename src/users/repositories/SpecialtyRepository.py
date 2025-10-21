from users.models.Specialty import Specialty

class SpecialtyRepository:
    @staticmethod
    def get_all():
        return Specialty.objects.all()
    
    @staticmethod
    def get_active():
        return Specialty.objects.filter(active=True)
    
    @staticmethod
    def get_by_id(specialty_id):
        try:
            return Specialty.objects.get(id=specialty_id)
        except Specialty.DoesNotExist:
            return None
    
    @staticmethod
    def create(name, description=None):
        specialty = Specialty(
            name=name,
            description=description
        )
        specialty.save()
        return specialty
    
    @staticmethod
    def update(specialty_id, name=None, description=None, active=None):
        specialty = SpecialtyRepository.get_by_id(specialty_id)
        if specialty:
            if name:
                specialty.name = name
            if description is not None:
                specialty.description = description
            if active is not None:
                specialty.active = active
            specialty.save()
        return specialty
    
    @staticmethod
    def delete(specialty_id):
        specialty = SpecialtyRepository.get_by_id(specialty_id)
        if specialty:
            specialty.delete()
            return True
        return False
