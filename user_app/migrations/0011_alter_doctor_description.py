# Generated by Django 4.1.7 on 2023-05-11 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0010_alter_doctor_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='description',
            field=models.CharField(help_text='DesCription', max_length=500),
        ),
    ]
