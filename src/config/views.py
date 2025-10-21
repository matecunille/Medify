from datetime import date
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Q

from consultations.models import STATUS_CANCELLED, STATUS_COMPLETED
from consultations.services import ConsultationService
from users.services import UserService
from users.services.SpecialtyService import SpecialtyService

@login_required
def home(request):
    doctors = UserService.get_doctors()
    patients = UserService.get_patients()
    consultations = ConsultationService.get_consultations_by_doctor(request.user.id).exclude(
        Q(status=STATUS_CANCELLED) | Q(status=STATUS_COMPLETED)
    )
    specialties = SpecialtyService.get_active_specialties()

    context = {'specialties': specialties, 'consultations': consultations, 'user': request.user, 'doctors': doctors, 'patients': patients, 'today': date.today().isoformat()}
    
    return render(request, 'home.html', context)
