from django.contrib import admin
from .models import Client


class ClientAdmin(admin.ModelAdmin):
    """
    Модель, которая описывает отображаемые в админ-панеле поля.
    """
    list_display = ['id', 'user', 'gender', 'image']
    list_filter = ['gender']
    search_fields = ['id', 'user']


admin.site.register(Client, ClientAdmin)
