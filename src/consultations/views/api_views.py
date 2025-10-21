from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from users.services import UserService

@login_required
def api_available_times(request):
    date = request.GET.get("date")
    doctor_id = request.GET.get("doctor")

    if not date or not doctor_id:
        return JsonResponse({"available_times": []})

    available_times = UserService.get_available_times(doctor_id, date)
    return JsonResponse({"available_times": available_times})
