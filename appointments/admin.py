from django.contrib import admin
from .models import appointment_booking


class AppointmentBookingAdmin(admin.ModelAdmin):
    list_display = (
        'date',
        'time',
        'service',
        'user',
        'complete',
    )


# Register your models here.
admin.site.register(appointment_booking, AppointmentBookingAdmin)
