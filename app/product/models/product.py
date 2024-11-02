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
    image = models.ImageField(upload_to="products", null=True, blank=True)

    def __str__(self):
        return self.title
