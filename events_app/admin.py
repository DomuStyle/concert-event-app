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

    fieldsets = [       
        # section named "Allgemein" (General) containing title, category, and date fields.
        ("Allgemein", {
            "fields": ["title", "category", "date"],
        }),
        # section named "Organisation" containing location and capacity fields, collapsed by default.
        ("Organisation", {
            "fields": ["location", "capacity"],
            "classes": ("collapse",)  # makes this section collapsible in the admin form.
        }),
    ]

    # enable a date-based navigation hierarchy in the admin interface based on the 'date' field.
    date_hierarchy = "date"


admin.site.register(EventCategory)
admin.site.register(Event, EventAdmin)
admin.site.register(Location)