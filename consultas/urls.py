from django.urls import path
from .views import  crear_consulta, cancelar_consulta, consulta_detalle, consulta_list_view, concluir_consulta

urlpatterns = [
    path('<int:pk>/', consulta_detalle, name='detalle_consulta'),
    path('<int:pk>/cancelar/', cancelar_consulta, name='cancelar_consulta'),
    path('<int:pk>/concluir/', concluir_consulta, name='concluir_consulta'),
    path('crear/', crear_consulta, name='crear_consulta'),
    path('crear/<int:pk>', crear_consulta, name='crear_consulta'),
    path('listar/', consulta_list_view, name='consultas')
]