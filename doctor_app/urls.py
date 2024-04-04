from django.contrib import admin
from django.urls import path, include
from .views import doctor_login, DoctorRegistrationView

urlpatterns = [
    path('login/', doctor_login, name='doctor_login'),
    path('register/', DoctorRegistrationView.as_view, name='doctor_register'),
]