import graphene

from .types import OrderType
from ...order.models import Order
from .mutations import OrderCreate


class OrderQueries(graphene.ObjectType):
    order = graphene.Field(
        OrderType, checkout_id=graphene.Argument(graphene.ID, description='ID of checkout')
    )
    orders = graphene.List(OrderType)

    def resolver_order(self, _info, checkout_id):
        order = Order.objects.filter(checkout_id=checkout_id).first()
        return order

    def resolve_orders(self, _info):
        orders = Order.objects.all()
        return orders


class OrderMutations(graphene.ObjectType):
    order_create = OrderCreate.Field()
