from django.contrib import admin

# Register your models here.
from .models import Product, ProductVar

admin.site.register(Product)
admin.site.register(ProductVar)
