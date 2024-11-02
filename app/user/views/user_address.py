from rest_framework import viewsets
from user.models import UserAddress
from user.serializers import UserAddressSerializer


class UserAddressViewSet(viewsets.ModelViewSet):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer
