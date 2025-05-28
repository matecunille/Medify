from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth import login, authenticate
from django.template.context_processors import request
from django.utils.http import url_has_allowed_host_and_scheme
from django.conf import settings

from .models import Usuario
from .services.UsuarioService import UsuarioService
from django.contrib import messages

def registro_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(password)
        confirm_password = request.POST.get('confirm_password')
        rol = request.POST.get('rol')

        if password != confirm_password:
            messages.error(request, "Las contrasenias deben coincidir!")
            return render(request, 'usuarios/registro.html')

        resultado = UsuarioService.crear_usuario(username=username, email=email, password=password, rol=rol)

        if resultado == 'usuario_duplicado':
            messages.error(request, "Nombre de usuario existente")
            return render(request, 'usuarios/registro.html')
        elif resultado == 'email_duplicado':
            messages.error(request, "Email existente")
            return render(request, 'usuarios/registro.html')
        elif resultado is None:
            messages.error(request, "Error inesperado al crear el usuario")
            return render(request, 'usuarios/registro.html')
        elif resultado is Usuario:
            messages.info(request,"Usuario creado!")
            return redirect('/usuarios/login/')

    return render(request, 'usuarios/registro.html')
class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario', max_length=150)
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')

def login_usuario(request):
    form = LoginForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            print(username,password)

            user = authenticate(request, username=username, password=password)
            print(user.__str__())
            if user is not None:
                login(request, user)
                return redirect('/consultas')
            else:
                messages.error(request, "Credenciales inválidas")
                return redirect('/usuarios/login')
        else:
            print("⚠️ Formulario inválido")
            print(f"Errores: {form.errors}")

    return render(request, 'usuarios/login.html', {'form': form})