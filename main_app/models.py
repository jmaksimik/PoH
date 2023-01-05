from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Doctor(models.Model): 
    SPECIALITIES = [ ('FM', 'Family Medicine'),
                 ('OR', 'Orthopedics'),
                 ('IM', 'Internal Medicine'),
               ]

    name = models.CharField(max_length=50)
    speciality = models.CharField(
        choices = SPECIALITIES,
        max_length = 5
    )

    def __str__(self): 
        return self.name

class Patient(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField(verbose_name = 'Birthdate')
    sex = models.CharField(
        verbose_name = 'Sex Assigned at Birth',
        choices = [('M', 'Male'), ('F', 'Female')],
        max_length = 1,
    )
    doctors = models.ManyToManyField(Doctor)


class Appointment(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(verbose_name='Appointment Date')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

