# Generated by Django 4.1.7 on 2023-05-31 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_diagnosis_symptoms'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Appointment',
        ),
    ]