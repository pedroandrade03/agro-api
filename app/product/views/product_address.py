from rest_framework import viewsets
from product.models import ProductAddress
from product.serializers import ProductAddressSerializer


class ProductAddressViewSet(viewsets.ModelViewSet):
    queryset = ProductAddress.objects.all()
    serializer_class = ProductAddressSerializer
