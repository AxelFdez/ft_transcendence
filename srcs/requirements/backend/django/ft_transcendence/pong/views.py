from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import User
from .serializers import UserListSerializer, UserDetailSerializer, UserSerializer

class MultipleSerializerMixin:

    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class UserViewSet(MultipleSerializerMixin, viewsets.ModelViewSet):

    serializer_class = UserListSerializer
    detail_serializer_class = UserDetailSerializer

    def get_serializer_class(self):
        if 'username' in self.request.query_params:
            return UserDetailSerializer
        return UserListSerializer

    def get_queryset(self):
        queryset = User.objects.filter(is_active=True)
        username = self.request.GET.get('username')
        if username:
            queryset = queryset.filter(username=username)
        return queryset

    def get(self, request):
        queryset = self.get_queryset()
        serializer = get_serializer_class(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")

