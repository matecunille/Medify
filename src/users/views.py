from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.template.context_processors import request
from django.utils.http import url_has_allowed_host_and_scheme
from django.conf import settings
from django.contrib import messages 

from .forms import UserForm, LoginForm, RegisterForm

def profile_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('home')
    else:
        form = UserForm(instance=request.user)
    return render(request, 'users/profile.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = form.cleaned_data['role']
            user.specialty = form.cleaned_data['specialty'] if user.role == 'doctor' else None
            
            if 'photo' in request.FILES:
                user.photo = request.FILES['photo']
            user.save()
            messages.success(request, "User created successfully!")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)  
        if form.is_valid():
            user = form.get_user()  
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')