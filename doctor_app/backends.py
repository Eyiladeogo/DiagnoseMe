from django.contrib.auth.backends import BaseBackend
from core.models import Doctor

class DoctorAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            doctor = Doctor.objects.get(username=username)
            if doctor.check_password(password):
                return doctor
        except Doctor.DoesNotExist:
            return None
