from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.core.exceptions import ValidationError

from consultas.models import Consulta
from usuarios.models import Usuario
from usuarios.services import UsuarioService
from .services.ConsultaService import ConsultaService

@login_required
def consulta_list_view(request):
    context = {
        'consultas' : ConsultaService.listar_consultas_por_paciente(request.user.id)
    }
    return render(request, 'consultas/lista.html', context)

@login_required
def consulta_detalle(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    if request.user != consulta.paciente and request.user != consulta.medico:
        return redirect('home')
    
    context = {
        'consulta': consulta,
        'usuario': request.user
    }
    return render(request, 'consultas/detalle.html', context)

@login_required
def cancelar_consulta(request, pk):
    consulta = ConsultaService.obtener_consulta_por_id(pk)
    if request.method == 'POST':
        ConsultaService.cancelar_consulta(consulta)
        return redirect('home')
    return render(request, 'consultas/cancelar.html', {'consulta': consulta})

@login_required
def crear_consulta(request, pk=None):
    consulta = None

    if pk:
        consulta = get_object_or_404(Consulta, id=pk)

    if request.method == 'POST':
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        descripcion = request.POST.get('descripcion')
        medico_id = request.POST.get('medico')

        if pk:
            # Actualizar consulta existente
            ConsultaService.actualizar_consulta(
                pk=pk,
                fecha=fecha,
                hora=hora,
                descripcion=descripcion
            )
            messages.success(request, 'Consulta actualizada correctamente')
        else:
            # Crear nueva consulta
            ConsultaService.crear_consulta(
                fecha=fecha,
                hora=hora,
                descripcion=descripcion,
                paciente=request.user.id,
                medico=medico_id
            )
            messages.success(request, 'Consulta creada correctamente')

        return redirect('home')
    
    fecha_param = request.GET.get('fecha') 
    medico_id = request.GET.get('medico_id') 
    medico_preseleccionado = None
    horarios_disponibles = []

    if medico_id and fecha_param:
        medico_preseleccionado = UsuarioService.obtener_por_id(medico_id)
        horarios_disponibles = UsuarioService.obtener_horarios_disponibles(medico_id, fecha_param)
        context = {
            'fecha': fecha_param,
            'medico_preseleccionado': medico_preseleccionado,
            'horarios_disponibles': horarios_disponibles,
        }
    else:
        horarios_disponibles = UsuarioService.obtener_horarios_disponibles(consulta.medico.id, consulta.fecha)
        context = {
            'consulta': consulta,  
            'horarios_disponibles' : horarios_disponibles
        }      
    
    return render(request, 'consultas/crear_consulta.html', context)