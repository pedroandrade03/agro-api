from rest_framework import serializers
from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=True)

    class Meta:
        model = Product
        exclude = "created_at", "updated_at"
