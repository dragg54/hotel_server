
from django.contrib import admin
from django.urls import path, include

from guest import views

urlpatterns = [
    path("", views.all_guests, name="all-guests"),
    path("<str:guest_id>", views.guest, name="guest")
]