from django.db.models import Q
from django_filters import rest_framework as filters

from .models import Client
from .utils import get_distance_in_meters


class ClientFilterSet(filters.FilterSet):
    """
    Кастомный фильтр
    distance - радиус поиска в метрах
    """
    distance = filters.NumberFilter(label='Расстояние(метры)', method='filter_method')

    class Meta:
        model = Client
        fields = ('gender', 'user__last_name', 'user__first_name', 'distance')

    def filter_method(self, queryset, field_name, value):
        """
        Метод который исключает из queryset клиентов не попадающих в радиус поиска.
        """
        if value:
            # получаем текущего авторизованного клиента
            current_client = Client.objects.get(user=self.request.user)
            # получаем всех остальных клиентов
            clients = queryset.filter(~Q(pk=current_client.pk))
            exclude_clients_pk = []
            for client in clients:
                # получаем позицию всех клиентов
                if get_distance_in_meters(current_client.get_point(), client.get_point()) > value:
                    # pk пользователей, которые не попадают в радиус поиска добавляются в список на исключение
                    exclude_clients_pk.append(client.pk)
            # исключаем не подходящих пользователей
            return clients.exclude(id__in=exclude_clients_pk)
        return queryset
