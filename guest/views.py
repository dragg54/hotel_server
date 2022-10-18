import json

from django.core import serializers
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from guest.forms import GuestAuth
from guest.models import Guest


def signup(request):
    if request == "POST":
        form = GuestAuth(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")


@csrf_exempt
def new_guest(request):
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    if first_name is not None and last_name is not None:
        user = Guest.objects.create(first_name=first_name, last_name=last_name)
        user.save()
        return HttpResponse(user)
    else:
        return HttpResponse("fields empty")


def all_guests(request):
    guests = Guest.objects.all()
    serialized_guests = serializers.serialize('json', guests)
    return HttpResponse(serialized_guests)


def guest(request, guest_id):
    hotel_guest = Guest.objects.filter(pk=guest_id)
    if hotel_guest:
        ser_guest = serializers.serialize("json", hotel_guest)
        return HttpResponse(ser_guest)
    else:
        return HttpResponseNotFound("Guest with id number " + str(guest_id) + " not found")

