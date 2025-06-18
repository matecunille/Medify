from usuarios.models.Especialidad import Especialidad

class EspecialidadRepository:
    @staticmethod
    def get_all():
        return Especialidad.objects.all()
    
    @staticmethod
    def get_activas():
        return Especialidad.objects.filter(activo=True)
    
    @staticmethod
    def get_by_id(especialidad_id):
        try:
            return Especialidad.objects.get(id=especialidad_id)
        except Especialidad.DoesNotExist:
            return None
    
    @staticmethod
    def create(nombre, descripcion=None):
        especialidad = Especialidad(
            nombre=nombre,
            descripcion=descripcion
        )
        especialidad.save()
        return especialidad
    
    @staticmethod
    def update(especialidad_id, nombre=None, descripcion=None, activo=None):
        especialidad = EspecialidadRepository.get_by_id(especialidad_id)
        if especialidad:
            if nombre:
                especialidad.nombre = nombre
            if descripcion is not None:
                especialidad.descripcion = descripcion
            if activo is not None:
                especialidad.activo = activo
            especialidad.save()
        return especialidad
    
    @staticmethod
    def delete(especialidad_id):
        especialidad = EspecialidadRepository.get_by_id(especialidad_id)
        if especialidad:
            especialidad.delete()
            return True
        return False
