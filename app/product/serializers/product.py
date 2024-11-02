from rest_framework import serializers
from product.models import Product
from .product_address import ProductAddressSerializer


class ProductSerializer(serializers.ModelSerializer):
    addresses = ProductAddressSerializer(many=True, read_only=True)
    image = serializers.ImageField(required=True)

    class Meta:
        model = Product
        fields = "__all__"
