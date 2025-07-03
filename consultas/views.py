from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from usuarios.services import UsuarioService
from .services.ConsultaService import ConsultaService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from consultas.models import Consulta
from usuarios.models import Usuario

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
def crear_consulta(request):
    if request.method == 'POST':
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        descripcion = request.POST.get('descripcion')
        paciente_id = request.user.id
        medico_id = request.POST.get('medico')

        ConsultaService.crear_consulta(fecha=fecha,hora= hora,descripcion= descripcion, paciente= paciente_id,medico= medico_id)

        return redirect('home')

    fecha_param = request.GET.get('fecha')
    medico_id = request.GET.get('medico_id')
    medico_preseleccionado = None
    horarios_disponibles = []

    if medico_id and fecha_param:
            medico_preseleccionado = UsuarioService.obtener_por_id(medico_id)
            print('Medico: ' + medico_preseleccionado.first_name)
            if medico_preseleccionado.rol != "medico":
                medico_preseleccionado = None
            else:
                horarios_disponibles = UsuarioService.obtener_horarios_disponibles(medico_id, fecha_param)
                
    context = {
        'fecha': fecha_param,
        'medico_preseleccionado': medico_preseleccionado,
        'horarios_disponibles': horarios_disponibles,
    }
    return render(request, 'consultas/crear_consulta.html', context)
