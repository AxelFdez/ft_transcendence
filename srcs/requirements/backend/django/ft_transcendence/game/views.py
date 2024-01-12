from django.shortcuts import render
from . import models, serializers
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404

class GameView(APIView):

	permissions_classes = [IsAdminUser]

	def get(self, request):
		game_entries = models.Game.objects.filter(id=id)
		serializer = serializers.GameSerializer(game_entries, many=True, context={'request': request})
		if serializer.is_valid():
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def post(self, request):
		serializer = serializers.GameSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def patch(self, request, id):
		get_object_or_404(models.Game, pk = id)
		game_entries = models.Game.objects.get(id=id)
		serializer = serializers.GameSerializer(game_entries, data=request.data, partial=True, context= { id : get_object_or_404(models.Game, pk = id)})
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)