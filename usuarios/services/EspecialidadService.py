from usuarios.repositories.EspecialidadRepository import EspecialidadRepository

class EspecialidadService:
    @staticmethod
    def obtener_todas_especialidades():
        return EspecialidadRepository.get_all()
    
    @staticmethod
    def obtener_especialidades_activas():
        return EspecialidadRepository.get_activas()
    
    @staticmethod
    def obtener_especialidad_por_id(especialidad_id):
        return EspecialidadRepository.get_by_id(especialidad_id)
    
    @staticmethod
    def crear_especialidad(nombre, descripcion=None):
        return EspecialidadRepository.create(nombre, descripcion)
    
    @staticmethod
    def actualizar_especialidad(especialidad_id, nombre=None, descripcion=None, activo=None):
        return EspecialidadRepository.update(especialidad_id, nombre, descripcion, activo)
    
    @staticmethod
    def eliminar_especialidad(especialidad_id):
        return EspecialidadRepository.delete(especialidad_id)
    
    @staticmethod
    def desactivar_especialidad(especialidad_id):
        return EspecialidadRepository.update(especialidad_id, activo=False)
