import graphene
from django.db.models import Sum
from graphene_django import DjangoObjectType
from ...order.models import Order, OrderComplet


class OrderType(DjangoObjectType):
    class Meta:
        model = Order
        fields = '__all__'

class OrderCompletType(DjangoObjectType):
    total_price = graphene.Decimal(description='Total price of order')

    class Meta:
        model = OrderComplet
        fields = '__all__'

    def resolve_total_price(self, _info):
        order = self.checkout.all().aggregate(total_checkout_price=Sum('price'))
        total_checkout_price = order['total_checkout_price']
        if not total_checkout_price:
            return self.price

