from django.urls import path
from django.contrib.auth import views as auth_views

from users.views import login_user, register_view, logout_view, profile_view

urlpatterns = [
    path('login/', login_user, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile')
]