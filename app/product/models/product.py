from core.models import BaseModel
from django.db import models


class Product(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.CharField(max_length=50)
    trade_option = models.BooleanField()
    whatsapp = models.CharField(max_length=20)
    is_service = models.BooleanField()
    working_hours = models.CharField(max_length=100)
    user = models.ForeignKey(
        "user.User", related_name="products", on_delete=models.CASCADE, null=True, blank=True
    )
    address = models.ForeignKey(
        "user.UserAddress", related_name="products", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.title
