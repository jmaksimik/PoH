from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save 
from django.dispatch import receiver

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
    birthdate = models.DateField(verbose_name = 'Birthdate', null=True, blank=True)
    sex = models.CharField(
        verbose_name = 'Sex Assigned at Birth',
        choices = [('M', 'Male'), ('F', 'Female')],
        max_length = 1,
        blank=True
    )
    doctors = models.ManyToManyField(Doctor, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created: 
        Patient.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs): 
    instance.patient.save()


class Appointment(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(verbose_name='Appointment Date')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} on {self.date}'
    
    def get_absolute_url(self):
        return reverse('appointments_index')


class Prescription(models.Model):
    name = models.CharField(max_length=50, verbose_name='Prescription Name')
    size = models.CharField(verbose_name='Dosage(mg)', max_length=50)
    doctor = models.ForeignKey(
        Doctor, 
        on_delete=models.CASCADE,
        verbose_name='Prescribing Doctor')
    prescribed = models.BooleanField(default=True, verbose_name='Currently Prescribed')

    def __str__(self):
        return self.name