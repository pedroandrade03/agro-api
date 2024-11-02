from django.urls import path, include
from rest_framework import routers
from user.views import UserViewSet, UserAddressViewSet

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"users_address", UserAddressViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
