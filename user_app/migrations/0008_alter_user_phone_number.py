# Generated by Django 4.1.7 on 2023-05-08 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0007_alter_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(help_text='Phone Number', max_length=11, unique=True),
        ),
    ]
