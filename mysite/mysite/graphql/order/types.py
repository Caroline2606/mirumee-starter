from graphene_django import DjangoObjectType

from ...order.models import Order


class OrderType(DjangoObjectType):
    class Meta:
        model = Order
        fields = '__all__'
