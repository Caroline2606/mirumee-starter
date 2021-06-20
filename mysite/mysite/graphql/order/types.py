from graphene_django import DjangoObjectType

from ...order.models import CheckoutComplet


class CheckoutCompletType(DjangoObjectType):
    class Meta:
        model = CheckoutComplet
        fields = '__all__'
