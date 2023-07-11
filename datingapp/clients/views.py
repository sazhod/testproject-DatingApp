from django.contrib.auth.models import User
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Client
from .serializers import ClientSerializer, UserSerializer


class ClientViewSet(viewsets.ViewSet):
    @swagger_auto_schema(responses={200: ClientSerializer(many=True)})
    def list(self, request):
        queryset = Client.objects.all()
        serializer = ClientSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ClientSerializer)
    def create(self, request):
        user_serializer = UserSerializer(data=request.data["user"])

        if user_serializer.is_valid():
            user = user_serializer.save()
            client = Client.objects.create(
                user=user,
                gender=request.data.get('gender', None),
                image=request.data.get('image', None)
            )
            client_serializer = ClientSerializer(client, many=False)
            return Response(client_serializer.data)

