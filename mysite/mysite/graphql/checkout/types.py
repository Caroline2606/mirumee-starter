import graphene

from graphene_django import DjangoObjectType
from django.db.models import Avg
from ...checkout.models import CheckoutLine, Checkout


class CheckoutType(DjangoObjectType):
    total_price = graphene.Decimal(description='Total price of checkout')

    def resolve_total_price(self, _info):
        checkout = self.user.all().aggregate(total_user_price=Avg('price'))
        total_user_price = checkout['total_user_price']
        if not total_user_price:
            return self.price

        return checkout['total_user_price']

    class Meta:
        model = Checkout
        fields = '__all__'


class CheckoutLineType(DjangoObjectType):
    total_price = graphene.Decimal(description='Total price of checkout')

    def resolve_total_price(self, _info):
        checkout_line = self.variant.all().aggregate(total_user_price=Avg('price'))
        total_variant_price = checkout_line['total_variant_price']
        if not total_variant_price:
            return self.price

        return checkout_line['total_variant_price']

    class Meta:
        model = CheckoutLine
        fields = '__all__'
