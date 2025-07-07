from datetime import date
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Q

from consultas.models import ESTADO_CANCELADO, ESTADO_CONCLUIDA
from consultas.services import ConsultaService
from usuarios.services import UsuarioService
from usuarios.services.EspecialidadService import EspecialidadService

@login_required
def home(request):
    medicos = UsuarioService.obtener_medicos()
    pacientes = UsuarioService.obtener_pacientes()
    consultas = ConsultaService.obtener_consultas_por_medico(request.user.id).exclude(
        Q(estado=ESTADO_CANCELADO) | Q(estado=ESTADO_CONCLUIDA)
    )
    especialidades = EspecialidadService.obtener_especialidades_activas()

    context = {'especialidades' : especialidades,'consultas': consultas,'user': request.user,'medicos': medicos, 'pacientes': pacientes, 'hoy': date.today().isoformat()}
    
    return render(request, 'home.html', context)
