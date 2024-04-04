from django.db import models

# from user_app.models import *

# from multiselectfield import MultiSelectField

from user_app.constants import *

class Symptom(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Diagnosis(models.Model):
    # name = MultiSelectField(choices=DIAGNOSIS, max_choices=3, max_length=1000, help_text='Category')
    name = models.CharField(max_length=100)
    # symptoms = models.ManyToManyField(Symptom, related_name='diagnoses')
    
    class Meta:
        verbose_name = 'Diagnosis'
        verbose_name_plural = 'Diagnoses'
    
    def __str__(self):
        return self.name
    
# class Appointment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     symptoms = models.ManyToManyField(Symptom)
#     diagnosis = models.ManyToManyField(Diagnosis, null=True, blank=True)
#     date = models.DateTimeField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user.username} - {self.doctor.user.username} - {self.date.strftime('%Y-%m-%d %H:%M:%S')}"
    

    
