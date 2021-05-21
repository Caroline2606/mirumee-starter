import graphene

from .types import CheckoutType
from ...checkout.models import Checkout
from .mutations import CheckoutCreate

class CheckoutQueries(graphene.ObjectType):
    checkout = graphene.Field(
        CheckoutType, id=graphene.Argument(graphene.ID, description="ID of checkout")
    )

    def reslove_checkout(self, _info, id):
        checkout = Checkout.objects.filter(id=id).first()
        return checkout



class CheckoutMutations(graphene.ObjectType):
    checkout_create = CheckoutCreate.Field()