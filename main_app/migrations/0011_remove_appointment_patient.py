# Generated by Django 3.2 on 2023-01-06 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_appointment_patient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='patient',
        ),
    ]