from django.db import models
from ..checkout.models import Checkout
from ..product.models import Product


class Order(models.Model):
    checkout_id = models.ForeignKey(Checkout, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
