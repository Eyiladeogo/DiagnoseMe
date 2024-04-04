from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth import logout


from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication

from .serializers import *

from .models import *

# @api_view(['POST',])
# def login_view(request):
#     if request.method == 'POST':
#         user = MyUser.objects.filter(username=request.username)
#         data = {
#             username
#         }
#         return()

# @api_view(['POST',])
# def logout_view(request):
#     if request.method == 'POST':
#         django_request = request._request  # Access the underlying Django request
#         logout(django_request)
#         Token.objects.filter(user=django_request.user).delete()
#         return Response({'detail': 'Logout successful.'})
#         # Token.objects.filter(user=request.user).delete()
#         # return Response({'detail':'Logout Successful'}, status=status.HTTP_200_OK)

# @api_view(['POST'])
# def logout_view(request):
#     if request.method == 'POST':
#         # Get the user token
#         user_token = request.auth
#         if user_token:
#             # Delete the token
#             user_token.delete()
#             return Response({'detail': 'Logout successful.'}, status=status.HTTP_200_OK)
#         else:
#             return Response({'detail': 'No token found for the user.'}, status=status.HTTP_400_BAD_REQUEST)
#     else:
#         return Response({'detail': 'Invalid request method.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
 
# class Logout(APIView):
#     def post(self, request, format=None):
#         # simply delete the token to force a login
#         request.user.auth_token.delete()
#         return Response(status=status.HTTP_200_OK)        

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'user_id': str(user.id)
        })

@api_view(['POST',])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['POST',])
def user_registration_view(request):
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            data['id'] = account.id
            data['username'] = account.username
            data['email'] = account.email
            data['phone_number'] = account.phone_number
            data['is_user'] = account.is_user
            
            token = Token.objects.get(user=account).key
            data['token'] = token
            
        else: 
            data = serializer.errors    
            
        return Response(data, status=status.HTTP_200_OK)
    
# @api_view(['POST',])
# def doctor_registration_view(request):
#     if request.method == 'POST':
#         serializer = DoctorRegistrationSerializer(data=request.data)
#         print('Before validation conditon')

#         if serializer.is_valid():
#             doctor = serializer.save()
#             category_ids = request.data.get('category',[])
#             categories = Diagnosis.objects.filter(id__in=category_ids)
#             doctor.category.set(categories)
#             token = Token.objects.get(user=doctor.user).key
#             data = {
#                 'username': doctor.user.username,
#                 'email': doctor.user.email,
#                 'description': doctor.description,
#                 'category': doctor.category,
#                 'is_doctor': doctor.user.is_doctor,
#                 'token': token
#             }
#             print('After validation condition')
#             return Response(data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST',])
def doctor_registration_view(request):
    if request.method == 'POST':
        serializer = DoctorRegistrationSerializer(data=request.data)
        print('Before validation condition')

        if serializer.is_valid():
            doctor = serializer.save()
            category_ids = request.data.get('category',[])
            categories = Diagnosis.objects.filter(id__in=category_ids)
            doctor.category.set(categories)
            token = Token.objects.get(user=doctor.user).key
            data = {
                'id': doctor.user.id,
                'username': doctor.user.username,
                'email': doctor.user.email,
                'description': doctor.description,
                'category': list(doctor.category.values_list('id', flat=True)),  # Serialize category to a list
                'is_doctor': doctor.user.is_doctor,
                'token': token
            }
            print('After validation condition')
            return Response(data, status=status.HTTP_201_CREATED)

        # Handle the serialization error
        try:
            serializer.errors['category'] = list(serializer.errors['category'])
        except KeyError:
            pass
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




#####################      ORIGINAL CODE      #####################
# @api_view(['POST',])
# def doctor_registration_view(request):
#     if request.method == 'POST':
#         serializer = DoctorRegistrationSerializer(data=request.data)
        
#         data = {}
        
#         if serializer.is_valid():
#             account = serializer.save()
            
#             data['username'] = account.username
#             data['email'] = account.email
#             data['description'] = account.description
#             data['category'] = account.category
#             data['is_doctor'] = account.is_doctor
            
#             token = Token.objects.get(user=account).key
#             data['token'] = token
            
#         else: 
#             data = serializer.errors    
            
#         return Response(data)


# @api_view(['POST',])
# def logout_view(request):
#     if request.method == 'POST':
#         # if request.user.is_authenticated():
#             request.user.auth_token.delete()
#             return Response(status=status.HTTP_200_OK)

# @api_view(['POST',])
# def registration_view(request):
#     if request.method == 'POST':
#         serializer = RegistrationSerializer(data=request.data)
        
#         data = {}
        
#         if serializer.is_valid():
#             account = serializer.save()
            
#             data['username'] = account.username
#             data['email'] = account.email
            
#             token = Token.objects.get(user=account).key
#             data['token'] = token
            
#         else: 
#             data = serializer.errors    
            
#         return Response(data)
