from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'doctors',DoctorViewSet, basename='doctor')  
router.register(r'diagnosis', DiagnosisViewSet, basename='diagnosis')
router.register(r'symptoms', SymptomViewSet, basename='symptom')
# router.register(r'appointments', AppointmentViewSet, basename='appointment')

urlpatterns = [
    path('', include(router.urls)),
    path('user_appointments/', UserAppointmentList.as_view(), name='user_appointment_list'),
    path('user_appointments/<int:pk>', UserAppointmentDetail.as_view(), name='user_appointment_detail'),
    path('doctor_appointments/', DoctorAppointmentList.as_view(), name='doctor_appointment_list'),
    path('doctor_appointments/<int:pk>', DoctorAppointmentDetail.as_view(), name='doctor_appointment_detail'),
    path('get_doctor_by_phone/<str:pk>', get_doctor_by_phone, name='get_doctor_by_phone'),
    path('get_doctors_by_category/', get_doctors_by_category, name ='get_doctors_by_category'),
    path('get_doctor_by_user_id/<int:pk>', get_doctor_by_user_id, name ='get_doctor_by_user_id')
]