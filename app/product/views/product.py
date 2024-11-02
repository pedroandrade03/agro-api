from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from product.models import Product
from product.serializers import ProductSerializer
from user.models import UserAddress


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=False, methods=["get"])
    def cities(self, request):
        user_address = UserAddress.objects.values_list("city", flat=True).distinct()
        user_address_list = [
            {"name": city} for city in user_address if city is not None
        ]
        return Response(user_address_list)
