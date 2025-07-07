from django.urls import path, include
from django.contrib import admin

from .views import home

urlpatterns = [
    path('', home , name='home'),
    path('admin/', admin.site.urls),
    path('consultas/',include('consultas.urls')),
    path('api/', include('consultas.api_urls')),
    path('usuarios/',include('usuarios.urls')),
]
