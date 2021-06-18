import graphene
from .types import OrderType, OrderCompletType
from ...order.models import Order, OrderComplet
from django.core.exceptions import ValidationError

class OrderCreateInput(graphene.InputObjectType):
    checkout_id = graphene.ID(required=True, description="ID of checkout")

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

class OrderCompletCreateInput(graphene.InputObjectType):
    price = graphene.Decimal(required=True)

class OrderCompletCreate(graphene.Mutations):
    order_complet = graphene.Field(OrderCompletType)

    class Arguments:
        input = OrderCompletCreateInput(required=True)
        order_id = graphene.ID(required=True)

    @classmethod
    def clean_price(cls, price):
        if price <= 0:
            raise ValidationError()

    @classmethod
    def clean_ID(cls, order_id):
        for order_id in OrderComplet:
            if order_id.objects.filter(id=id).exists():
                return True
            else:
                raise ValidationError
        return order_id


    @classmethod
    def clean_input(cls, data):
        cls.clean_price((input['pricr']))
        cls.clean_ID(input['order_id'])

        return data

    @classmethod
    def mutate(cls, root, _info, input, order_id):
        cleaned_input = cls.clean_input(input)

        order_complet = OrderComplet.objects.create(order_id=order_id, **cleaned_input)

        return OrderCompletCreate(order_complet=order_complet)
