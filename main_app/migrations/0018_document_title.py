# Generated by Django 3.2 on 2023-01-10 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0017_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Document Title'),
        ),
    ]
