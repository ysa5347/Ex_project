from importlib.metadata import requires
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import get_user_model,authenticate
from django.contrib.auth.models import update_last_login
from .models import CustomUser

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

User = get_user_model()

class UserLoginSerializer(serializers.Serializer):
    userID = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)
    
    def validate(self, data):
        userID = data.get("userID", None)
        password = data.get("password", None)
        user = authenticate(userID=userID, password=password)

        if user is None:
            return {
                'userID': 'None'
            }
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        return {
            'userID': user.userID,
            'token': jwt_token
        }

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