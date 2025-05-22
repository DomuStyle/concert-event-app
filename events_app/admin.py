from django.contrib import admin
from .models import EventCategory, Event, Location

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    # Specify the fields to display in the admin list view for Events.
    list_display = ("title", "category", "location", "date")


admin.site.register(EventCategory)
admin.site.register(Event, EventAdmin)
admin.site.register(Location)