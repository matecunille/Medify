from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.core.exceptions import ValidationError

from consultations.models import Consultation
from users.models import User
from users.services import UserService
from ..services.ConsultationService import ConsultationService

@login_required
def consultation_list_view(request):
    if request.user.role == "doctor":
        context = {
            'consultations' : ConsultationService.get_consultations_by_doctor(request.user.id)
        }
    else:
        context = {
            'consultations' : ConsultationService.list_consultations_by_patient(request.user.id)
        }
    return render(request, 'consultations/list.html', context)

@login_required
def consultation_detail(request, pk):
    consultation = get_object_or_404(Consultation, pk=pk)
    if request.user != consultation.patient and request.user != consultation.doctor:
        return redirect('home')
    
    context = {
        'consultation': consultation,
        'user': request.user
    }
    return render(request, 'consultations/detail.html', context)

@login_required
def cancel_consultation(request, pk):
    consultation = ConsultationService.get_consultation_by_id(pk)
    if consultation:
        ConsultationService.cancel_consultation(consultation)
        return redirect('home')
    return redirect('home')

@login_required
def complete_consultation(request, pk):
    consultation = ConsultationService.get_consultation_by_id(pk)
    if consultation:
        ConsultationService.complete_consultation(consultation)
        return redirect('home')
    return redirect('home')

@login_required
def create_consultation(request, pk=None):
    consultation = None

    if pk:
        consultation = get_object_or_404(Consultation, id=pk)

    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')
        description = request.POST.get('description')
        doctor_id = request.POST.get('doctor')

        if pk:
            # Update existing consultation
            ConsultationService.update_consultation(
                pk=pk,
                date=date,
                time=time,
                description=description
            )
            messages.success(request, 'Consultation updated successfully')
            return redirect('consultations')
        else:
            # Create new consultation
            ConsultationService.create_consultation(
                date=date,
                time=time,
                description=description,
                patient=request.user.id,
                doctor=doctor_id
            )
            messages.success(request, 'Consultation created successfully')
            return redirect('home')
        
    
    date_param = request.GET.get('date') 
    doctor_id = request.GET.get('doctor_id') 
    preselected_doctor = None
    available_times = []

    if doctor_id and date_param:
        preselected_doctor = UserService.get_by_id(doctor_id)
        available_times = UserService.get_available_times(doctor_id, date_param)
        context = {
            'date': date_param,
            'preselected_doctor': preselected_doctor,
            'available_times': available_times,
        }
    else:
        available_times = UserService.get_available_times(consultation.doctor.id, consultation.date)
        context = {
            'consultation': consultation,  
            'available_times' : available_times
        }      
    
    return render(request, 'consultations/create_consultation.html', context)