from django.contrib.auth.forms import UserCreationForm
from django import forms

from guest.models import Guest


class GuestAuth(UserCreationForm):
    email = forms.EmailField()
    password2 = forms.CharField(max_length=15)

    class Meta:
        model = Guest
        fields = ["email", "password1", "password2"]