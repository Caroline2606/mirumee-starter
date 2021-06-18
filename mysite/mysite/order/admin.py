from django.contrib import admin

# Register your models here.
from .models import Order, OrderComplet

admin.site.register(Order)
admin.site.register(OrderComplet)