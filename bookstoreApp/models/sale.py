from django.db import models
from .productModels import Product
from .user import User


class Sale(models.Model):
    product = models.ForeignKey(Product, related_name='sold_products', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='purchases', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    datetime= models.DateTimeField(auto_now=True)