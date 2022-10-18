from django.db import models

from guest.models import Guest


class Room(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    number = models.IntegerField(max_length=None)
    type = models.CharField(max_length=50)
    price = models.IntegerField(max_length=None)
    booked = models.BooleanField()
    booked_by = models.OneToOneField(Guest, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/", default=None)

    def __str__(self):
        return self.name
