# Generated by Django 4.1.7 on 2023-05-15 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0012_alter_doctor_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, help_text='Authentication Token', max_length=255, null=True),
        ),
    ]
