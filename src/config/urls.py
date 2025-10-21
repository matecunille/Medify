from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from .views import home

urlpatterns = [
    path('', home , name='home'),
    path('admin/', admin.site.urls),
    path('consultations/',include('consultations.urls')),
    path('api/', include('consultations.api_urls')),
    path('users/',include('users.urls')),
]

# Se cargan las fotos y archivos estáticos
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)