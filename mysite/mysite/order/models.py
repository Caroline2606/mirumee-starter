from django.db import models
from ..checkout.models import Checkout


class CheckoutComplet(models.Model):
    checkout_id = models.ForeignKey(Checkout, on_delete=models.CASCADE)
