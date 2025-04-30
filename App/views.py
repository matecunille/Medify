from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Usuario


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Email o contraseña incorrectos')

    return render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = email.split('@')[0]
        password = request.POST['password']

        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'Ese email ya está registrado')
        else:
            user = Usuario.objects.create_user(email=email, username=username, password=password)
            login(request, user)
            return redirect('home')

    return render(request, 'register.html')


@login_required
def home(request):
    return render(request, 'app/home.html')