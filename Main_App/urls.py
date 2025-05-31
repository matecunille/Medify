"""
URL configuration for TP_Programacion_3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from datetime import date

from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import path, include

from consultas.services import ConsultaService
from usuarios.services import UsuarioService


@login_required
def home(request):
    medicos = UsuarioService.obtener_medicos()
    pacientes = UsuarioService.obtener_pacientes()
    consultas = ConsultaService.obtener_consultas_por_medico(request.user.id)
    return render(request, 'home.html', {'consultas': consultas,'user': request.user,'medicos': medicos, 'pacientes': pacientes, 'hoy': date.today().isoformat()})

urlpatterns = [
    path('', home , name='home'),
    path('admin/', admin.site.urls),
    path('consultas/',include('consultas.urls')),
    path('usuarios/',include('usuarios.urls')),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
