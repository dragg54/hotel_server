
from django.contrib import admin
from django.urls import path, include

from room import views

urlpatterns = [
    path("", views.get_rooms, name="all-room"),
    path("<str:room_id>", views.get_room_by_id, name="room")
]