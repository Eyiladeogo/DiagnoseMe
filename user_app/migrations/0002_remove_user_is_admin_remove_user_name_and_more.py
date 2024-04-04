# Generated by Django 4.1.7 on 2023-05-07 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(help_text='Phone Number', max_length=11, unique=True),
        ),
    ]