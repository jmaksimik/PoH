# Generated by Django 3.2 on 2023-01-10 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0018_document_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='file_type',
            new_name='file_category',
        ),
        migrations.AddField(
            model_name='document',
            name='url',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
