# Generated by Django 4.1.7 on 2023-06-01 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_delete_appointment'),
        ('user_app', '0016_remove_doctor_category_appointment_doctor_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='diagnosis',
            field=models.ManyToManyField(blank=True, to='core.diagnosis'),
        ),
    ]
