from django.db import models

from ..product.models import ProductVariant


class CheckoutLine(models.Model):
    variant = models.ForeignKey(ProductVariant, related_name='variant', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    checkout = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)


class Checkout(models.Model):
    user = models.ForeignKey(CheckoutLine, related_name='user', on_delete=models.CASCADE)
    lines = models.ForeignKey(CheckoutLine, on_delete=models.CASCADE)
    user_email = models.EmailField(null=False, blank=False, max_length=30)



