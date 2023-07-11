from django.contrib import admin
from .models import Client, Likes


class ClientAdmin(admin.ModelAdmin):
    """
    Модель, которая описывает отображаемые в админ-панеле поля клиента.
    """
    list_display = ['id', 'user', 'gender', 'image']
    list_filter = ['gender']
    search_fields = ['id', 'user']


class LikesAdmin(admin.ModelAdmin):
    """
        Модель, которая описывает отображаемые в админ-панеле поля симпатий.
        """
    list_display = ['id', 'from_client', 'to_client']
    search_fields = ['id', 'from_client', 'to_client']


admin.site.register(Client, ClientAdmin)
admin.site.register(Likes, LikesAdmin)
