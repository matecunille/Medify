from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import Usuario
from .services.UsuarioService import UsuarioService
from .services.EspecialidadService import EspecialidadService
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

from .models import Usuario
from .services import UsuarioService

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
        
        if self.instance and self.instance.username == username:
            return username
        if UsuarioService.buscar_por_username(username):
            raise ValidationError("Nombre de usuario ya está en uso.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        
        if self.instance and self.instance.email == email:
            return email
        if UsuarioService.buscar_por_email(email):
            raise ValidationError("Email ya está registrado.")
        return email

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