from django.urls import path
from .views.views import create_consultation, cancel_consultation, consultation_detail, consultation_list_view, complete_consultation

urlpatterns = [
    path('<int:pk>/', consultation_detail, name='consultation_detail'),
    path('<int:pk>/cancel/', cancel_consultation, name='cancel_consultation'),
    path('<int:pk>/complete/', complete_consultation, name='complete_consultation'),
    path('create/', create_consultation, name='create_consultation'),
    path('create/<int:pk>', create_consultation, name='create_consultation'),
    path('list/', consultation_list_view, name='consultations')
]