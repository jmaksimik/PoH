from django.contrib import admin
# Register your models here.
from .models import Patient, Appointment, Doctor 

admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Doctor)