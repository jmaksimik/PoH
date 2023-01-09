from django.forms import ModelForm 
from .models import Patient, Prescription
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.utils.crypto import get_random_string
from django.core.exceptions import ValidationError

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(
        min_length = 1,
        max_length = 20,
        required = True
    )
    last_name = forms.CharField(
        min_length = 1,
        max_length = 50,
        required = True
    )
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

    def clean(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Email Exists')
        return self.cleaned_data

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = get_random_string(20)
        if commit:
            user.save()
        return user 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})


class UserForm(ModelForm):
    class Meta: 
        model = User
        fields = ['first_name', 'last_name', 'email']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})

class PatientForm(ModelForm):
    class Meta: 
        model = Patient 
        fields = ['birthdate', 'sex', 'doctors']

class PrescriptionForm(ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required-field'
    name = forms.CharField(widget=forms.TextInput
        (attrs={
            "class": "form-control ",
            "id": "prescriptionName",
            "placeholder": "Medication Name"
        }))
    size = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control ",
            "id": "prescriptionStrength",
            "placeholder": "Available Doses"
        }
    ))
    instructions = forms.CharField(widget=forms.Textarea(
        attrs={
            "rows": 3
        }
    ))
    class Meta:
        model = Prescription
        fields = ['name', 'size', 'doctor', 'instructions', 'notes', 'prescribed']

    # def __int__(self, *args, **kwargs):
    #     super().__init__(args, **kwargs)
    #     for field in self.fields:
    #         print(field)
    #         new_data = {
    #             "placeholder": f'Recipe {str(field)}',
    #             "class": "form-control",
                
    #         }

    #         self.fields[str(field)].widget.attrs.update(
    #             new_data
    #         )
    #     self.fields['name'].label = "NAME HERE"
        # self.fields['name'].widget.attrs.update({'class': "form-control-2"})