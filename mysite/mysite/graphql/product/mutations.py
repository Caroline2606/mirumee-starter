from decimal import Decimal

import graphene

from .types import ProductType, ProductVariantType
from ...product.models import Product

class ProductCreateInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    price = graphene.Decimal(required=True)
    description = graphene.String(required=True)
    quantity = graphene.Int()

class ProductCreate(graphene.Mutation):
    product = graphene.Field(ProductType)

    class Arguments:
        input = ProductCreateInput(required=True)

    def clean_input(self, input):
        input(ProductCreateInput)
        for product in input:
            price = product['price']
        Decimal(price)
        return input

    def mutate(self, root, info, input):
        cleaned_input = self.clean_input(input)

        product = Product.objects.create(**cleaned_input)

        return ProductCreate(product=product)

class ProductVariantCreateInput(graphene.InputObjectType):
    product = graphene.String(required=True)
    name = graphene.String(required=True)
    sku = graphene.String(required=True)
    price = graphene.Decimal(required=True)

class ProductVariantCreate(graphene.Mutation):
    product = graphene.Field(ProductVariantType)

    class Arguments:
        input = ProductVariantCreateInput(required=True)

    def clean_input(self, input):
        return input

    def mutate(self, root, info, input):
        cleaned_input = self.clean_input(input)

        product = Product.objects.create(**cleaned_input)

        return ProductVariantCreate(product=product)

