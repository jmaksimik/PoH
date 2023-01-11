from django.contrib import admin
# Register your models here.
from .models import Patient, Appointment, Doctor, Prescription, Insurance, Document

admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Doctor)
admin.site.register(Prescription)
admin.site.register(Document)
admin.site.register(Insurance)
