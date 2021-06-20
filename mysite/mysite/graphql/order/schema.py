import graphene

from .types import CheckoutCompletType
from ...order.models import CheckoutComplet
from .mutations import CheckoutCompletCreate


class CheckoutCompletQueries(graphene.ObjectType):
    checkout_complet = graphene.Field(
        CheckoutCompletType, id=graphene.Argument(graphene.ID, description='ID of checkout complet')
    )
    checkouts_complet = graphene.List(CheckoutCompletType)


    def resolver_checkout_complet(self, _info, checkout_id):
        checkout_complet = CheckoutComplet.objects.filter(checkout_id=checkout_id).first()
        return checkout_complet

    def resolve_checkouts_complet(self, info):
        checkouts_complet = CheckoutComplet.objects.all()
        return checkouts_complet


class CheckoutCompletMutations(graphene.ObjectType):
    checkout_complet_create = CheckoutCompletCreate.Field()
