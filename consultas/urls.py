from django.urls import path
from .views import  crear_consulta, cancelar_consulta, consulta_detalle

urlpatterns = [
    path('<int:pk>/', consulta_detalle, name='detalle_consulta'),
    path('<int:pk>/cancelar/', cancelar_consulta, name='cancelar_consulta'),
    path('crear/', crear_consulta, name='crear_consulta'),
]