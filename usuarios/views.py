from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth import login, authenticate, logout
from django.template.context_processors import request
from django.utils.http import url_has_allowed_host_and_scheme
from django.conf import settings

from .models import Usuario
from .services.UsuarioService import UsuarioService
from .services.EspecialidadService import EspecialidadService
from django.contrib import messages

def logout_view(request):
    logout(request)
    return redirect('login')

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'username', 'email', 'dni', 'foto']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'username': 'Usuario',
            'email': 'Email',
            'dni': 'DNI',
            'foto': 'Foto de perfil'
        }
        widgets = {
            field: forms.TextInput(attrs={'class': 'form-control'})
            for field in fields if field != 'foto'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['foto'].widget = forms.FileInput(attrs={'class': 'form-control'})
        self.fields['foto'].required = False
        
    def clean_username(self):
        username = self.cleaned_data['username']
        # Solo validar si el username cambió y no es el del usuario actual
        if self.instance and self.instance.username == username:
            return username
        if UsuarioService.buscar_por_username(username):
            raise ValidationError("Nombre de usuario ya está en uso.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        # Solo validar si el email cambió y no es el del usuario actual
        if self.instance and self.instance.email == email:
            return email
        if UsuarioService.buscar_por_email(email):
            raise ValidationError("Email ya está registrado.")
        return email

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

from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control w-100'})
    )
    password2 = forms.CharField(
        label='Confirmar Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control w-100'})
    )
    
    rol = forms.ChoiceField(
        choices=Usuario.ROL_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    especialidad = forms.ModelChoiceField(
        queryset=EspecialidadService.obtener_especialidades_activas(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'dni', 'foto', 'rol', 'especialidad']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['foto'].widget = forms.FileInput(attrs={'class': 'form-control'})
        self.fields['foto'].required = False

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
        if cleaned_data.get('rol') == 'medico' and not cleaned_data.get('especialidad'):
            self.add_error('especialidad', 'La especialidad es obligatoria para médicos')
        return cleaned_data

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.rol = form.cleaned_data['rol']
            user.especialidad = form.cleaned_data['especialidad'] if user.rol == 'medico' else None
            # Asignar la foto si fue subida
            if 'foto' in request.FILES:
                user.foto = request.FILES['foto']
            user.save()
            messages.success(request, "¡Usuario creado exitosamente!")
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/crear_usuario.html', {'form': form})

from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Usuario'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Contraseña'
        })

def login_usuario(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)  # Pasamos el request al form
        if form.is_valid():
            user = form.get_user()  # Usamos el usuario ya autenticado por el form
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'usuarios/login.html', {'form': form})