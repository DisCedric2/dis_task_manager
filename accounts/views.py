from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from accounts.serializers import UserRegisterSerializer

# Create your views here.

# generic class-based view for user registration
class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]
