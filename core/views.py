from django.shortcuts import render
from django.http import JsonResponse
# from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, viewsets, status
from rest_framework.decorators import api_view

from .serializers import SymptomSerializer, DoctorSerializer, DiagnosisSerializer, AppointmentSerializer, UserSerializer
from .models import Symptom, Diagnosis

from user_app.models import *

class UserViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAdminUser]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
class SymptomViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAdminUser]
    serializer_class = SymptomSerializer
    queryset = Symptom.objects.all()
    
class DoctorViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAdminUser]
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    
class DiagnosisViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAdminUser]
    serializer_class = DiagnosisSerializer
    queryset = Diagnosis.objects.all()
    
class UserAppointmentList(APIView):
    def get(self, request):
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors)      
        

class UserAppointmentDetail(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"detail": "User object does not exist"}, status=status.HTTP_404_NOT_FOUND) 
        appointments = Appointment.objects.filter(user=user)
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"detail": "User object does not exist"}, status=status.HTTP_404_NOT_FOUND) 
        appointments = Appointment.objects.filter(user=user)
        serializer = AppointmentSerializer(appointments, many=True, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"detail": "User object does not exist"}, status=status.HTTP_404_NOT_FOUND) 
        appointments = Appointment.objects.filter(user=user)
        appointments.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class UserAppointmentDetail(APIView):
#     def get(self, request, pk):
#         user = User.objects.get(pk=pk)
#         appointments = Appointment.objects.filter(user=user)
#         serializer = AppointmentSerializer(appointments, data=request.data)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def put(self, request, pk):
#         user = User.objects.get(pk=pk)
#         appointments = Appointment.objects.filter(user=user)
#         serializer = AppointmentSerializer(appointments, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors)
        
#     def delete(self, request, pk):
#         user = User.objects.get(pk=pk)
#         appointments = Appointment.objects.get(user=user)
#         appointments.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
class DoctorAppointmentList(APIView):
    def get(self, request):
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors)

class DoctorAppointmentDetail(APIView):
    def get(self, request, pk):
        try:
            doctor = Doctor.objects.get(pk=pk)
        except Doctor.DoesNotExist:
            return Response({"detail": "Doctor object does not exist"}, status=status.HTTP_404_NOT_FOUND)          
        appointments = Appointment.objects.filter(doctor=doctor)
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        try:
            doctor = Doctor.objects.get(pk=pk)
        except Doctor.DoesNotExist:
            return Response({"detail": "Doctor object does not exist"}, status=status.HTTP_404_NOT_FOUND)
        appointments = Appointment.objects.filter(doctor=doctor)
        serializer = AppointmentSerializer(appointments, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors)
    
    def delete(self, request, pk):
        try:
            doctor = Doctor.objects.get(pk=pk)
        except Doctor.DoesNotExist:
            return Response({"detail": "Doctor object does not exist"}, status=status.HTTP_404_NOT_FOUND)
        appointments = Appointment.objects.filter(doctor=doctor)
        appointments.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
# class AppointmentViewSet(viewsets.ModelViewSet):
#     # permission_classes = [permissions.IsAdminUser]
#     serializer_class = AppointmentSerializer
#     queryset = Appointment.objects.all()
    
    
@api_view(['GET',])
def get_doctor_by_phone(request, pk):
    if request.method == 'GET':
        user = User.objects.get(phone_number=pk)
        doctor = Doctor.objects.get(user=user)
        serializer = DoctorSerializer(doctor)
        if user and user.is_doctor:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Doctor object not found"}, status=status.HTTP_404_NOT_FOUND)
    else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['POST',])
def get_doctors_by_category(request):
    if request.method == 'POST':
        data = request.data
        categories = data.get('category',[])  # Retrieve the list of categories from the request body
        print(categories)
        doctors = Doctor.objects.filter(category__in=categories).distinct()
        print(doctors)
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid request method'})
    
@api_view(['GET',])
def get_doctor_by_user_id(request, pk):
    if request.method == 'GET':
        try:
            doctor = Doctor.objects.get(user=pk)
        except Doctor.DoesNotExist:
            return Response({"detail": "Doctor object does not exist"}, status=status.HTTP_404_NOT_FOUND)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data, status=status.HTTP_200_OK)