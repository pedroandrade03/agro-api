from rest_framework import serializers
from user.models import User
from .user_address import UserAddressSerializer


class UserSerializer(serializers.ModelSerializer):
    addresses = UserAddressSerializer(many=True, read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = "password", "username", "email", "addresses"
