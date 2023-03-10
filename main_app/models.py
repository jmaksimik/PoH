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

# Do we really want cascase delete on these??
class Prescription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=50, verbose_name='Prescription Name')
    size = models.CharField(verbose_name='Dosage(mg)', max_length=50)
    doctor = models.ForeignKey(
        Doctor, 
        on_delete=models.CASCADE,
        verbose_name='Prescribing Doctor',
        blank=True, null=True)
    prescribed = models.BooleanField(default=True, verbose_name='Currently Prescribed')
    instructions = models.TextField(max_length=250, verbose_name="Use Instructions", blank=True, null=True)
    notes = models.TextField(max_length=250, verbose_name="Patient Notes", blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('prescriptions_index')

class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_category = models.CharField(
        choices=[('ML', 'Labwork'), ('IM', 'Imaging'), ('GD', 'General Documents')],
        verbose_name='File Type',
        max_length=2
    )
    title = models.CharField(max_length=50, verbose_name = 'Document Title', blank=True, null=True)
    notes = models.CharField(max_length=250, verbose_name='Notes', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.title} @ {self.url}'

class Insurance(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    insurance_company = models.CharField(
        verbose_name = 'Insurance Company',
        choices = [('UH', 'UnitedHealth'), ('KF', 'Kaiser Foundation'), ('AI', 'Anthem Inc'),
        ('CC', 'Centene Corp'), ('HU','Humana'), ('CV', 'CVS'), ('HC', 'Health Care Service Corporation'),
        ('CH', 'Cigna  Health'), ('MH', 'Molina Healthcare'), ('IH', 'Independence Health Group')],
        max_length= 2,
        blank=True, null=True
    )
    subscriber = models.CharField(max_length=50, verbose_name='Name', blank=True)
    member = models.CharField(max_length=20, verbose_name='Member ID', blank=True)
    group = models.CharField(max_length=20, verbose_name='Group', blank=True)

    def __str__(self):
        return f"{self.insurance_company} - {self.member}"