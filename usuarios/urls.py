from django.urls import path
from django.contrib.auth import views as auth_views

from usuarios.views import login_usuario, registro_view, logout_view

urlpatterns = [
    path('login/', login_usuario, name='login'),
    path('registro/', registro_view, name='registro'),
    path('logout/',logout_view,name='logout')
]