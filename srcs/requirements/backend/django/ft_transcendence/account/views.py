from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, UserProfileSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import UserProfile
from django.shortcuts import get_object_or_404, redirect


class UserRegisterView(APIView):
    @csrf_exempt
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            if User.objects.filter(email=email).exists():
                return Response({"error": "Email already exists"}, status=status.HTTP_400_BAD_REQUEST)
            elif email == None:
                return Response({"error": "Email needed"}, status=status.HTTP_400_BAD_REQUEST)
            user = User.objects.create_user(
                username = serializer.validated_data.get('username'),
                password = serializer.validated_data.get('password'),
                email=email,
            )
            UserProfile.objects.create(user=user)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AllUserView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class UserView(APIView):
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class ProfileView(APIView):

    # def get_permissions(self):
    #     if self.request.method == 'GET':
    #         return [permissions.AllowAny()]
    #     return [permissions.IsAuthenticated()]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        user_profile = UserProfile.objects.filter(user=user).first()
        serializer = UserProfileSerializer(user_profile, context={'request': request})
        return Response(serializer.data)

    def patch(self, request):
        user = request.user
        user_profile = UserProfile.objects.filter(user=user).first()  # Obtenez le profil de l'utilisateur
        serializer = UserProfileSerializer(user_profile, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            serializer = UserSerializer(user, data=request.data, partial=True, context={'request': request})
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        user = request.user
        user_profile = UserProfile.objects.filter(user=user).first()  # Obtenez le profil de l'utilisateur
        if user_profile:
            user_profile.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)

class getProfileView(APIView):
    def get(self, request, username):
        user_profile = get_object_or_404(UserProfile, user__username=username)
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    def get(self):
        return Response(status=status.HTTP_204_NO_CONTENT)

