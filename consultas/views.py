from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from usuarios.services import UsuarioService
from .services.ConsultaService import ConsultaService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from consultas.models import Consulta

class ConsultaListView(LoginRequiredMixin, ListView):
    template_name = "consultas/lista.html"
    context_object_name = "consultas"

    def get_queryset(self):
        return ConsultaService.listar_consultas()

@method_decorator(login_required, name='dispatch')
class ConsultaDetailView(DetailView):
    model = Consulta
    template_name = "consultas/detalle.html"
    context_object_name = "consulta"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usuario'] = self.request.user
        return context

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
