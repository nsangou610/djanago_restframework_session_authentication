from django.contrib.auth import authenticate, login, logout
from userapp.models import User
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from userapp.serializers import UserSerializer
from django.conf import settings


class CheckAuthenticatedView(APIView):
    permission_classes=[AllowAny]
    def get(self, request):
        if request.user.is_authenticated:
            return Response({'isAuthenticated': True})
        else:
            return Response({'isAuthenticated': False})
 

class RegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.create(serializer.validated_data)
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        user = authenticate(request, email=email, password=password)
     
        if user is not None:
            if user.is_active:
                login(request, user)
                return Response({'detail':'Logged in successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Email or Password is incorrect.'}, status=status.HTTP_400_BAD_REQUEST)
      
class UserDetailView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        data = serializer.data
        data['is_staff'] = request.user.is_staff
        return Response(data)
    
    def patch(self, request):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ChangePasswordView(APIView):
    def post(self, request):
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        user = request.user

        if not user.check_password(old_password):
            return Response({'detail': 'Invalid old password.'}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password)
        user.save()
        return Response({'detail': 'Password changed successfully.'}, status=status.HTTP_200_OK)
     

class DeleteAccountView(APIView):
    def delete(self, request):
        user = request.user
        user.delete()
        logout(request)
        return Response({'detail': 'Account deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'detail': 'Logged out successfully.'}, status=status.HTTP_200_OK)
    
