from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password', 'avatar', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'last_login', 'bio', 'avatar', 'games_id']
