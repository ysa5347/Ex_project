from importlib.metadata import requires
from rest_framework import serializers

from django.contrib.auth import get_user_model

from .models import CustomUser
User = get_user_model()

class UserCreateSerializer(serializers.Serializer):
    userID = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    def create(self, validated_data):
        user = CustomUser.objects.create(
            userID = validated_data['userID'],
            email = validated_data['email'],
        )
        user.set_password(validated_data['password'])

        user.save()
        return user