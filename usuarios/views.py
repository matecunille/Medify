from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.template.context_processors import request
from django.utils.http import url_has_allowed_host_and_scheme
from django.conf import settings
from django.contrib import messages 

from .forms import UsuarioForm, LoginForm, RegistroForm

def perfil_view(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Perfil actualizado exitosamente!")
            return redirect('home')
    else:
        form = UsuarioForm(instance=request.user)
    return render(request, 'usuarios/perfil.html', {'form': form})

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.rol = form.cleaned_data['rol']
            user.especialidad = form.cleaned_data['especialidad'] if user.rol == 'medico' else None
            
            if 'foto' in request.FILES:
                user.foto = request.FILES['foto']
            user.save()
            messages.success(request, "¡Usuario creado exitosamente!")
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/crear_usuario.html', {'form': form})

def login_usuario(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)  
        if form.is_valid():
            user = form.get_user()  
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'usuarios/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')