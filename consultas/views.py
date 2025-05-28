from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Consulta
from .services.ConsultaService import ConsultaService
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from consultas.models import Consulta
class ConsultaListView(LoginRequiredMixin, ListView):
    template_name = "consultas/lista.html"
    context_object_name = "consultas"

    def get_queryset(self):
        return ConsultaService.listar_consultas()

class ConsultaDetailView(LoginRequiredMixin, DetailView):
    template_name = "consultas/detalle.html"
    context_object_name = "consulta"

    def get_object(self, **kwargs):
        consulta_id = self.kwargs.get("pk")
        return get_object_or_404(Consulta, pk=consulta_id)

@login_required
def crear_consulta(request):

    Usuario = get_user_model()
    if request.method == 'POST':
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        descripcion = request.POST.get('descripcion')
        paciente_id = request.POST.get('paciente')
        medico_id = request.POST.get('medico')

        ConsultaService.crear_consulta(fecha, hora, descripcion, paciente_id, medico_id)

        return redirect('lista_consultas')

    fecha_param = request.GET.get('fecha')
    pacientes = Usuario.objects.filter(rol='paciente')
    medicos = Usuario.objects.filter(rol='medico')
    context = {
        'fecha': fecha_param,
        'pacientes': pacientes,
        'medicos': medicos
    }
    return render(request, 'consultas/Crear_consulta.html', context)
