from graphene_django import DjangoObjectType

from ...product.models import Product, ProductVar

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = '__all__'

class ProductVariantType(DjangoObjectType):
    class Meta:
        model = ProductVar
        fields = '__all__'
