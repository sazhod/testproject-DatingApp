from typing import Any

from django.contrib.auth.models import User
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Client
from .serializers import ClientSerializer, UserSerializer


class ClientViewSet(viewsets.ViewSet):
    """
    Класс, в которм реализована логика всех запросов связанных с клиентами.
    """
    @swagger_auto_schema(responses={200: ClientSerializer(many=True)})
    def list(self, request: Any) -> Response:
        """
        api/clients/
        Возвращает информацию о всех клиентах
        """
        queryset = Client.objects.all()
        serializer = ClientSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ClientSerializer)
    def create(self, request):
        """
        api/clients/create/
        Принимает данные из формы добавления клиента.
        Создаёт нового пользователя(User) и клиента(Client)
        Возвращает данные клиента или UserSerializer.errors
        """
        user_serializer = UserSerializer(data=request.data)

        if user_serializer.is_valid():
            user = user_serializer.save()
            client = Client.objects.create(user=user)

            gender = request.data.get('gender', None)
            if gender:
                client.gender = gender

            image = request.data.get('image', None)
            if image:
                client.image = image

            client.save()
            client_serializer = ClientSerializer(client, many=False)
            return Response(client_serializer.data)
        return Response(user_serializer.errors)

