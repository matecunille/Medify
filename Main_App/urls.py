from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from .views import home

urlpatterns = [
    path('', home , name='home'),
    path('admin/', admin.site.urls),
    path('consultas/',include('consultas.urls')),
    path('api/', include('consultas.api_urls')),
    path('usuarios/',include('usuarios.urls')),
]

# Se cargan las fotos
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)