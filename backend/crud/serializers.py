from operator import mod
from rest_framework import serializers
from .models import Users
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','name','email')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user