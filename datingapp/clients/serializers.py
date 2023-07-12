from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Client


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'email', 'username', 'password')


class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Client
        fields = ('id', 'gender', 'image', 'user')
