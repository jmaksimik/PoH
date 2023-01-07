# Generated by Django 3.2 on 2023-01-07 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_alter_prescription_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='instructions',
            field=models.TextField(blank=True, max_length=250, null=True, verbose_name='Use Instructions'),
        ),
        migrations.AddField(
            model_name='prescription',
            name='notes',
            field=models.TextField(blank=True, max_length=250, null=True, verbose_name='Patient Notes'),
        ),
    ]
