from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField(verbose_name = 'Birthdate')
    sex = models.CharField(
        verbose_name = 'Sex Assigned at Birth',
        choices = ['M', 'F'],
    )

class Appointments(models.Model): 
    date = models.DateField(verbose_name='Appointment Date')

