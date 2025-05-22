from django.contrib import admin
from .models import EventCategory, Event, Location

# Register your models here.

admin.site.register(EventCategory)
admin.site.register(Event)
admin.site.register(Location)