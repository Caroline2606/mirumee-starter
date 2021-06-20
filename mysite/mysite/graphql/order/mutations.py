import graphene

from .types import CheckoutCompletType
from ...order.models import CheckoutComplet


class CheckoutCompletCreateInput(graphene.InputObjectType):
    checkout_id = graphene.ID(required=True, description="ID of checkout")


class CheckoutCompletCreate(graphene.Mutation):
    checkout_complet = graphene.Field(CheckoutCompletType)

    class Arguments:
        checkout_id = graphene.ID(required=True)

    @classmethod
    def mutate(cls, root, _info, checkout_id):

        checkout_complet = CheckoutComplet.objects.create(checkout_id=checkout_id)

        return CheckoutCompletCreate(checkout_complet=checkout_complet)
