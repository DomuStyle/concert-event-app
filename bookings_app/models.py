from django.db import models
from django import forms

# Create your models here.
from events_app.models import Event

class Participant(models.Model):
    first_name = models.CharField(max_length=100, help_text="Vorname")
    last_name = models.CharField(max_length=100, help_text="Nachname")

    email = models.EmailField(unique=True, help_text="E-Mail-Adresse")
    # slugField to store a URL-friendly version of the full name, optional and defaults to empty.
    full_name = models.SlugField(max_length=200, blank=True, default="")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    booking_date = models.DateField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.participant} → {self.event.title}"