from django.forms import ModelForm 
from .models import Patient, Prescription
from django.contrib.auth.models import User
from django import forms

class UserForm(ModelForm):
    class Meta: 
        model = User
        fields = ['first_name', 'last_name', 'email']

class PatientForm(ModelForm):
    class Meta: 
        model = Patient 
        fields = ['birthdate', 'sex', 'doctors']

class PrescriptionForm(ModelForm):
    class Meta:
        model = Prescription
        fields = ['name', 'size', 'doctor', 'prescribed']