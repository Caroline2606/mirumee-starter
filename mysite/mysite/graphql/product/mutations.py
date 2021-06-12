import graphene
from ..core.utils import staff_member_required
from .types import ProductType, ProductVariantType
from ...product.models import Product, ProductVariant
from django.core.exceptions import ValidationError


class ProductCreateInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    price = graphene.Decimal(required=True)
    description = graphene.String(required=True)
    quantity = graphene.Int()


class ProductCreate(graphene.Mutation):
    product = graphene.Field(ProductType)

    class Arguments:
        input = ProductCreateInput(required=True)

    @classmethod
    def clean_input(cls, input):
        return input

    @classmethod
    @staff_member_required
    def mutate(cls, root, info, input):
        cleaned_input = cls.clean_input(input)

        product = Product.objects.create(**cleaned_input)

        return ProductCreate(product=product)

class ProductVariantCreateInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    sku = graphene.Int(required=True)
    price = graphene.Decimal(required=True)

class ProductVariantCreate(graphene.Mutation):
    product_variant = graphene.Field(ProductVariantType)

    class Arguments:
        input = ProductVariantCreateInput(required=True)
        product_id = graphene.ID(required=True)

    @classmethod
    def clean_price(cls, price):
        if price <= 0:
            raise ValidationError
        return price

    @classmethod
    def clean_ID(cls, product_id):
        for product_id in ProductVariant:
            if product_id.objects.filter(id=id).exists():
                return True
            else:
                raise ValidationError
        return product_id

    @classmethod
    def clean_SKU(cls, sku, variant_id):

        try:
            sku = ProductVariant.objects.get(variant_id=variant_id)
        except sku.objects.filter(variant_id=variant_id).exists():
            raise ValidationError

    @classmethod
    def clean_input(cls, data, price, product_id, sku, variant_id):
        cls.clean_price(price)
        cls.clean_ID(product_id)
        cls.clean_SKU(sku, variant_id)

        return data



    @classmethod
    @staff_member_required
    def mutate(cls, root, _info, input, product_id):
        cleaned_input = cls.clean_input(input)

        product_variant = ProductVariant.objects.create(product_id=product_id, **cleaned_input)

        return ProductVariantCreate(product_variant=product_variant)

