from rest_framework import serializers
from .models import Menu,Booking

# following is for customizing the djoser user creation to enable the name in the api
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from django.contrib.auth.models import User
class CustomUserSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        model=User
        fields=['first_name','last_name','email','username','password']

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model=Menu
        fields='__all__'
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields=['name','no_of_guests','booking_date']