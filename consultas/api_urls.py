from django.urls import path
from . import api_views

urlpatterns = [
    path('horarios-disponibles/', api_views.api_horarios_disponibles, name='api_horarios_disponibles'),
]