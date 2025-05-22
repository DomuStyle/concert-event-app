from django.contrib import admin
from .models import Participant, Booking
# Register your models here.


class BookingAdmin(admin.ModelAdmin):
    # make the booking_date field read-only in the add/edit forms, as it’s auto-set on creation.
    readonly_fields = ['booking_date']

admin.site.register(Participant)
admin.site.register(Booking, BookingAdmin)