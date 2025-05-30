from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth import login, authenticate, logout
from django.template.context_processors import request
from django.utils.http import url_has_allowed_host_and_scheme
from django.conf import settings

from .models import Usuario
from .services.UsuarioService import UsuarioService
from django.contrib import messages

def logout_view(request):
    logout(request)
    return redirect('login')

class RegistroForm(forms.Form):
    nombre = forms.CharField(label='Nombre',max_length=15)
    apellido = forms.CharField(label='Apellido',max_length=15)
    username = forms.CharField(label='Usuario', max_length=150)
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirmar contraseña')
    rol = forms.ChoiceField(choices=Usuario.ROL_CHOICES, label='Rol')
    dni = forms.CharField(label='DNI', max_length=20, required=False)
    especialidad = forms.CharField(label='Especialidad', max_length=100, required=False)

    def clean_username(self):
        username = self.cleaned_data['username']
        if UsuarioService.buscar_por_username(username):
            raise ValidationError("Nombre de usuario ya está en uso.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if UsuarioService.buscar_por_email(email):
            raise ValidationError("Email ya está registrado.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        rol = cleaned_data.get('rol')
        especialidad = cleaned_data.get('especialidad')

        if password and confirm_password and password != confirm_password:
            raise ValidationError("Las contraseñas no coinciden")

        if rol == 'medico' and not especialidad:
            raise ValidationError("La especialidad es obligatoria para médicos")

        return cleaned_data

def registro_view(request):
    form = RegistroForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        data = form.cleaned_data
        user = UsuarioService.crear_usuario(
            username=data['username'],
            email=data['email'],
            password=data['password'],
            rol=data['rol'],
            dni=data.get('dni'),
            especialidad=data.get('especialidad') if data['rol'] == 'medico' else None,
            first_name=data.get('nombre'),
            last_name=data.get('apellido')
        )
        if user is None:
            messages.error(request, "Error inesperado al crear el usuario")
        else:
            messages.success(request, "¡Usuario creado exitosamente!")
            return redirect('/usuarios/login/')

    return render(request, 'usuarios/registro.html', {'form': form})
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