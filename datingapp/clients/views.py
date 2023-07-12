from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render

from drf_yasg.utils import swagger_auto_schema
from django_filters import rest_framework as filters

from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, action
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .filters import ClientFilterSet
from .models import Client, Likes
from .serializers import ClientSerializer, UserSerializer
from .utils import send_email


class ClientListAPIView(generics.ListAPIView):
    """
    api/list/
    Класс который отвечает за отображение клиентов с учетом фильтрации по полям:
    gender, last_name, first_name
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ClientFilterSet

class ClientViewSet(viewsets.ViewSet):
    """
    Класс, в которм реализована логика создания и симпатий клиентов.
    """
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

    @permission_classes([IsAuthenticated])
    def likes(self, request, pk=None):
        """
        api/clients/<int:pk>/match
        При отправке пост запроса от авторизированного клиента сохраняет симпатию в БД(если её её нет).
        Проверяет на совпадение симпатии. При совпадении отправляет email обоим клиентам и соответсвующее сообщение.
        При отсутсвии совместной симпатии отправляет соответсвующее сообщение.
        """
        from_client = Client.objects.get(pk=request.user.pk)
        to_client = Client.objects.get(pk=pk)

        if not Likes.objects.filter(from_client=from_client.pk, to_client=to_client.pk).exists():
            Likes.objects.create(from_client=from_client, to_client=to_client)

        if Likes.objects.filter(from_client=to_client.pk, to_client=from_client.pk).exists():
            send_email(from_client, to_client)
            send_email(to_client, from_client)
            return Response({'Message': f'У вас взаимная симпатия с пользователем "{to_client}"! '
                                        f'Вот его почта "{to_client.user.email}"'})
        return Response({'Message': f'Вы отправили свою симпатию пользователю "{to_client}"'})


class LoginUser(LoginView):
    """
    Представление, которое необходимо для отображения формы авторизаии.
    Необходимо для проверки симпатий.
    """
    form_class = AuthenticationForm
    template_name = 'clients/index.html'
