from django.urls import path
from .views import api_views

urlpatterns = [
    path('available-times/', api_views.api_available_times, name='api_available_times'),
]