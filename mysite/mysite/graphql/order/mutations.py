import graphene

from .types import OrderType
from ...order.models import Order


class OrderCreateInput(graphene.InputObjectType):
    checkout_id = graphene.ID(required=True, description="ID of checkout")
    product_id = graphene.ID(required=True, description="ID of product")
    price = graphene.Decimal(required=True)

class OrderCreate(graphene.Mutation):
    order = graphene.Field(OrderType)

    class Arguments:
        input = OrderCreateInput(required=True)

    @classmethod
    def clean_input(cls, input):
        return input

    @classmethod
    def mutate(cls, root, info, input):
        cleaned_input = cls.clean_input(input)

        order = Order.objects.create(**cleaned_input)

        return OrderCreate(order=order)
