from rest_framework import serializers
from user.models import UserAddress


class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        exclude = "created_at", "updated_at", "user"
