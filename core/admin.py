from django.contrib import admin
from.models import Symptom, Diagnosis
from user_app.models import Appointment
# from user_app.models import Doctor

admin.site.register(Symptom)
admin.site.register(Diagnosis)
# admin.site.register(Doctor)
admin.site.register(Appointment)