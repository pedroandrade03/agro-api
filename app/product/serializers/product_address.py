from rest_framework import serializers
from product.models import ProductAddress


class ProductAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAddress
        fields = "__all__"
