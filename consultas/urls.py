from django.urls import path
from .views import ConsultaDetailView

urlpatterns = [
    path('<int:pk>/', ConsultaDetailView.as_view(), name='detalle'),
]