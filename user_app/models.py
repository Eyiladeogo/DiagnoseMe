from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
# from multiselectfield import MultiSelectField

from .constants import *
from core.models import *

from rest_framework.authtoken.models import Token

class User(AbstractUser):
    # name = models.CharField(max_length=100, help_text='Name')
    email = models.EmailField(unique=True, null=True)
    phone_number = models.CharField(max_length=11, unique=True, help_text='Phone Number')
    is_user = models.BooleanField('Is User', default=False)
    is_doctor = models.BooleanField('Is Doctor', default=False)
    # user_type = models.PositiveSmallIntegerField(choices=user_constants.USER_TYPE_CHOICES) #should only be used when choices are > 3
    
    # def __str__(self):
    #     return self.name
# class User(AbstractUser):
#     # Existing fields
#     email = models.EmailField(unique=True, null=True)
#     phone_number = models.CharField(max_length=11, unique=True, help_text='Phone Number')
#     is_user = models.BooleanField('Is User', default=False)
#     is_doctor = models.BooleanField('Is Doctor', default=False)
    
#     # New field
#     token = models.CharField(max_length=255, blank=True, null=True, help_text='Authentication Token')
    
#     def save(self, *args, **kwargs):
#         # Set the token value before saving the user
#         if self.pk is None:
#             token = Token.objects.create(user=self)
#             self.token = token.key
        
#         super().save(*args, **kwargs)
    
class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=500, help_text='Description')
    # category = MultiSelectField(choices=DIAGNOSIS, max_choices=5, max_length=1000, help_text='Category')
    category = models.ManyToManyField(Diagnosis)
    experience = models.IntegerField(help_text='Experience')
    
    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created: 
        Token.objects.create(user=instance)
        
        
class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    symptoms = models.ManyToManyField(Symptom)
    diagnosis = models.ManyToManyField(Diagnosis, blank=True)
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.doctor.user.username} - {self.date.strftime('%Y-%m-%d %H:%M:%S')}"
    
