from django.shortcuts import render
from django.contrib.auth import authenticate

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, status

from core.models import Doctor
from core.serializers import DoctorSerializer

from user_app.serializers import TokenSerializer

@api_view(['POST'])
def doctor_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None and user.is_active and user.is_doctor:
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'username': user.username,
            'email': user.email,
            'token': token.key,
        })
    else:
        return Response({'error': 'Invalid login credentials.'}, status=400)



class DoctorRegistrationView(generics.CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            doctor = serializer.save()
            token, _ = Token.objects.get_or_create(user=doctor)
            token_serializer = TokenSerializer(instance=token)
            data = {
                'username': doctor.username,
                'email': doctor.email,
                'token': token_serializer.data['key']
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


