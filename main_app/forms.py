from django.forms import ModelForm 
from .models import Patient
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    class Meta: 
        model = User
        fields = ['first_name', 'last_name', 'email']

class PatientForm(forms.ModelForm):
    class Meta: 
        model = Patient 
        fields = ['birthdate', 'sex', 'doctors']