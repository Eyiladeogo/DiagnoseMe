# Generated by Django 4.1.7 on 2023-05-11 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0009_doctor_id_alter_doctor_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
