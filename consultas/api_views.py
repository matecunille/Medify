from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from usuarios.services import UsuarioService

@login_required
def api_horarios_disponibles(request):
    fecha = request.GET.get("fecha")
    medico_id = request.GET.get("medico")

    if not fecha or not medico_id:
        return JsonResponse({"horarios": []})

    horarios = UsuarioService.obtener_horarios_disponibles(medico_id, fecha)
    return JsonResponse({"horarios": horarios})
