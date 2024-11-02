from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from product.models import Product
from product.serializers import ProductSerializer, CitySerializer
from user.models import UserAddress


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    @action(detail=False, methods=["get"])
    def cities(self, request):
        user_address = UserAddress.objects.values_list("city", flat=True).distinct()
        
        return Response(CitySerializer(user_address, many=True).data)
    
