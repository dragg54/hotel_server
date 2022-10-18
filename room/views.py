from django.core import serializers
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from room.models import Room


def get_rooms(request):
    rooms = Room.objects.all()
    if rooms is not None:
        rooms_ser = serializers.serialize("json", rooms)
        return HttpResponse(rooms_ser)
    else:
        return HttpResponseNotFound("Not Found")


def get_room_by_id(request, room_id):
    room = Room.objects.filter(pk=room_id)
    if room:
        ser_room = serializers.serialize("json", room)
        return HttpResponse(ser_room)
    else:
        return HttpResponseNotFound("Guest with id number " + str(room_id) + " not found")
