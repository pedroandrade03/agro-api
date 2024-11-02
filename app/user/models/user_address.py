from core.models import BaseModel
from django.db import models


class UserAddress(BaseModel):
    user = models.ForeignKey(
        "user.User", related_name="addresses", on_delete=models.CASCADE
    )
    cep = models.CharField(max_length=10)
    street = models.CharField(max_length=255)
    neighborhood = models.CharField(max_length=255)
    number = models.CharField(max_length=10)
    complement = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.street}, {self.number}"
