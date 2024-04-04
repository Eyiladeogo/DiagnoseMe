# from django.contrib.auth.models import User
from rest_framework import serializers

from .models import *
from .constants import *


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'phone_number', 'first_name', 'last_name', 'is_user', 'is_doctor'] 
        extra_kwargs = {'password': {'write_only': True}}

    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        email = self.validated_data['email']
        username = self.validated_data['username']
        phone_number = self.validated_data['phone_number']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        is_user = self.validated_data['is_user']
        is_doctor = self.validated_data['is_doctor']
        
        if len(phone_number) != 11:
            raise serializers.ValidationError('Phone Number must be eleven digits!')
        
        if password != password2:
            raise serializers.ValidationError('Password mismatch!')
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email already exists!')
        
        account = User(email=email, username=username, phone_number=phone_number, first_name=first_name, last_name=last_name, is_user=is_user, is_doctor=is_doctor)
        account.set_password(password)
        account.save()
        
        return account
    
# class DoctorRegistrationSerializer(serializers.ModelSerializer):
#     password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
#     user = UserRegistrationSerializer()

#     # Additional fields specific to the Doctor model
#     description = serializers.CharField()
#     category = serializers.ListField(child=serializers.ChoiceField(choices=DIAGNOSIS))
#     experience = serializers.IntegerField()

#     def create(self, validated_data):
#         user_data = validated_data.pop('user')
#         password = user_data.pop('password')
#         password2 = validated_data.pop('password2')

#         if password != password2:
#             raise serializers.ValidationError('Password mismatch!')

#         # Create the User instance
#         user = User.objects.create_user(password=password, **user_data)

#         # Create the Doctor instance
#         doctor = Doctor.objects.create(user=user, **validated_data)

#         return doctor

#     class Meta:
#         model = Doctor
#         fields = ['user', 'password2', 'description', 'category', 'experience']

#         extra_kwargs = {'password': {'write_only': True}}

    
#####################      THIS IS THE ONE WITH THE ATTRIBUTE ERROR FOR IS_DOCTOR      #####################
class DoctorRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    # Include the fields from the UserRegistrationSerializer
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    phone_number = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    is_user = serializers.BooleanField(default=False)
    is_doctor = serializers.BooleanField(default=False)

    # Additional fields specific to the Doctor model
    description = serializers.CharField()
    category = serializers.PrimaryKeyRelatedField(many=True, queryset = Diagnosis.objects.all())
    experience = serializers.IntegerField()
    

    def create(self, validated_data):
        # Extract the user registration fields
        user_data = {
            'username': validated_data['username'],
            'email': validated_data['email'],
            'password': validated_data['password'],
            'password2': validated_data['password2'],
            'phone_number': validated_data['phone_number'],
            'is_user': validated_data['is_user'],
            'is_doctor': validated_data['is_doctor'],
            'first_name': validated_data['first_name'],
            'last_name': validated_data['last_name'],
        }
        if validated_data['password'] != validated_data['password2']:
            raise serializers.ValidationError('Password mismatch!')

        user_data.pop('password2', None)
        # user_data.pop('is_doctor', None)
        # user_data.pop('is_user', None)
        
        # Create the User instance
        user = User.objects.create_user(**user_data)

        # Extract the doctor-specific fields
        doctor_data = {
            'user': user,
            'description': validated_data['description'],
            # 'category': validated_data['category'],
            'experience': validated_data['experience'],
        }

        # Create the Doctor instance
        doctor = Doctor.objects.create(**doctor_data)
        doctor.category.set(validated_data['category'])
        
        def to_representation(self, instance):
            representation = super().to_representation(instance)
            representation['category'] = instance.category.values_list('id', flat=True)
            return representation

        return doctor

    class Meta:
        model = Doctor
        fields = ['username', 'email', 'password', 'password2', 'phone_number', 'is_user', 'is_doctor', 'description', 'category', 'experience', 'first_name', 'last_name']


#####################      ORIGINAL CODE      #####################
# class DoctorRegistrationSerializer(serializers.ModelSerializer):
#     password2 = serializers.CharField(
#         style={'input_type': 'password'}, write_only=True)

#     class Meta:
#         model = Doctor
#         fields = ['username', 'email', 'password', 'password2']
#         extra_kwargs = {'password': {'write_only': True}}

#     def save(self):
#         password = self.validated_data['password']
#         password2 = self.validated_data['password2']
#         email = self.validated_data['email']
#         username = self.validated_data['username']
#         phone_number = self.validated_data['phone_number']
#         first_name = self.validated_data['first_name']
#         last_name = self.validated_data['last_name']
#         is_doctor = self.validated_data['is_user']
        
#         if password != password2:
#             raise serializers.ValidationError('Password mismatch')
        
#         if Doctor.objects.filter(email=email):
#             raise serializers.ValidationError('Email already exists')
        
#         account = Doctor(email=email, username=username, phone_number=phone_number, first_name=first_name, last_name=last_name, is_doctor=is_doctor)
#         account.set_password(password)
#         account.save()
        
#         return account
    
# from rest_framework import serializers
# from rest_framework.authtoken.models import Token

# class TokenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Token
#         fields = ('key',)
