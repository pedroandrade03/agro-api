from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet, ProductAddressViewSet

router = routers.DefaultRouter()
router.register(r"products", ProductViewSet)
router.register(r"productaddresses", ProductAddressViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
