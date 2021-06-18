import graphene

from .types import OrderType, OrderCompletType
from ...order.models import Order, OrderComplet
from .mutations import OrderCreate, OrderCompletCreate


class OrderQueries(graphene.ObjectType):
    order = graphene.Field(
        OrderType, checkout_id=graphene.Argument(graphene.ID, description='ID of checkout')
    )
    orders = graphene.List(OrderType)
    order_complet = graphene.Field(
        OrderCompletType, order_id=graphene.Argument(graphene.ID, description='ID of order')
    )

    def resolver_order(self, _info, checkout_id):
        order = Order.objects.filter(checkout_id=checkout_id).first()
        return order

    def resolve_orders(self, _info):
        orders = Order.objects.all()
        return orders

    def resolve_order_complet(self, _info, order_id):
        OrderComplet = Order.objects.all()
        return OrderComplet.objects.filter(order_id=order_id)

class OrderMutations(graphene.ObjectType):
    order_create = OrderCreate.Field()
    order_complet_create = OrderCompletCreate.Field()