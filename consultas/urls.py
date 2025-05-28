from django.urls import path
from .views import ConsultaDetailView, ConsultaListView, crear_consulta

urlpatterns = [
    path('', ConsultaListView.as_view(), name='lista_consultas'),
    path('<int:pk>/', ConsultaDetailView.as_view(), name='detalle_consulta'),
    path('crear/', crear_consulta, name='crear_consulta'),
]