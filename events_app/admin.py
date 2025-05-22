from django.contrib import admin
from .models import EventCategory, Event, Location

# Register your models here.

class EventAdmin(admin.ModelAdmin):

    # specify the fields to display in the admin list view for Events.
    list_display = ("title", "category", "location", "date")

    # define fields that can be searched in the admin search bar.
    search_fields = ("title", "date")
    
    # Add filters to the admin list view, allowing filtering by category.
    list_filter = ["category"]


admin.site.register(EventCategory)
admin.site.register(Event, EventAdmin)
admin.site.register(Location)