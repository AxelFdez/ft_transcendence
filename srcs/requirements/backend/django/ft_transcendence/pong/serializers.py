from rest_framework import serializers
from .models import User

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'avatar', 'bio', 'is_active', 'is_superuser', 'is_staff', 'created_at', 'updated_at']

    def get_user(self, instance):
        queryset = User.objects.all()
        serializer = UserDetailSerializer(queryset, many=True)
        return serializer.data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'avatar', 'bio', 'is_active', 'is_superuser', 'is_staff', 'created_at', 'updated_at']
