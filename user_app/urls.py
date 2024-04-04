from django.urls import path
# from rest_framework.authtoken.views import obtain_auth_token

from .views import *

urlpatterns = [
    path('login/', CustomObtainAuthToken.as_view(), name='login'),
    path('patient/register/', user_registration_view, name='patient_register'),
    path('doctor/register/', doctor_registration_view, name='doctor_register'),
    path('logout/', logout_view, name='logout'),
]