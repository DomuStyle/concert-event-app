from django.contrib import admin
from .models import Participant, Booking
# Register your models here.


class BookingAdmin(admin.ModelAdmin):
    # make the booking_date field read-only in the add/edit forms, as it’s auto-set on creation.
    readonly_fields = ['booking_date']
    # add a filter sidebar to filter bookings by the 'confirmed' field (True/False).
    list_filter = ["confirmed"]

    list_display = ("event", "participant", "booking_date", "confirmed")

class ParticipantAdmin(admin.ModelAdmin):

    list_display = ("first_name", "last_name", "full_name", "email")
    # Auto-populate the full_name slug field based on first_name and last_name in the admin form.
    prepopulated_fields = {"full_name": ("first_name", "last_name")}

admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Booking, BookingAdmin)