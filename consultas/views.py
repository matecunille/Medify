from django.views.generic import ListView, DetailView
from .models import Consulta

class ConsultaListView(ListView):
    model = Consulta
    template_name = "consultas/lista.html"
    context_object_name = "consultas"

class ConsultaDetailView(DetailView):
    model = Consulta
    template_name = "consultas/detalle.html"
    context_object_name = "consulta"
