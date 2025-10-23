from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .repositories import GuestRepository

guest_repo = GuestRepository()

from .repositories import HotelRepository

hotel_repo = HotelRepository()

def index(request):
    return render(request, 'core/index.html', {'title': 'Управління готелем'})

def guest_list(request):
    guests = hotel_repo.guests.get_all()
    return render(request, 'core/guest_list.html', {'guests': guests})


def guest_detail(request, guest_id):
    guest = guest_repo.get_by_id(guest_id)
    if guest is None:
        return HttpResponse(f"Гостя з ID {guest_id} не існує", status=404)
    return HttpResponse(f"Ім'я гостя: {guest.first_name} {guest.last_name}")