from rest_framework import serializers
from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=True)
    city = serializers.SerializerMethodField()

    class Meta:
        model = Product
        exclude = "created_at", "updated_at"

    def get_city(self, obj):
        if obj.address:
            return obj.address.city
        return None
