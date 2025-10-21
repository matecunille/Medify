from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import User
from .services.UserService import UserService
from .services.SpecialtyService import SpecialtyService
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

from .models import User
from .services import UserService

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Username'
        })
        self.fields['username'].label = 'Username'
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password'
        })
        self.fields['password'].label = 'Password'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'dni', 'photo']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'username': 'Username',
            'email': 'Email',
            'dni': 'DNI',
            'photo': 'Profile Photo'
        }
        widgets = {
            field: forms.TextInput(attrs={'class': 'form-control'})
            for field in fields if field != 'photo'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['photo'].widget = forms.FileInput(attrs={'class': 'form-control'})
        self.fields['photo'].required = False
        
    def clean_username(self):
        username = self.cleaned_data['username']
        
        if self.instance and self.instance.username == username:
            return username
        if UserService.find_by_username(username):
            raise ValidationError("Username is already taken.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        
        if self.instance and self.instance.email == email:
            return email
        if UserService.find_by_email(email):
            raise ValidationError("Email is already registered.")
        return email

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control w-100'})
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control w-100'})
    )
    
    role = forms.ChoiceField(
        choices=User.ROLE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    specialty = forms.ModelChoiceField(
        queryset=SpecialtyService.get_active_specialties(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'dni', 'photo', 'role', 'specialty']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['photo'].widget = forms.FileInput(attrs={'class': 'form-control'})
        self.fields['photo'].required = False

    def clean_username(self):
        username = self.cleaned_data['username']
        if UserService.find_by_username(username):
            raise ValidationError("Username is already taken.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if UserService.find_by_email(email):
            raise ValidationError("Email is already registered.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('role') == 'doctor' and not cleaned_data.get('specialty'):
            self.add_error('specialty', 'Specialty is required for doctors')
        return cleaned_data