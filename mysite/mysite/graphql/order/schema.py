import graphene

from .types import CheckoutCompletType
from ...order.models import CheckoutComplet
from .mutations import CheckoutCompletCreate


class CheckoutCompletQueries(graphene.ObjectType):
    checkout_complet = graphene.Field(
        CheckoutCompletType, checkout_id=graphene.Argument(graphene.ID, description='ID of checkout')
    )
    checkouts_complet = graphene.List(CheckoutCompletType)

    # checkout_complet_line = graphene.Field(
    #     CheckoutCompletLineType,
    #     id=graphene.Argument(graphene.ID, description="ID of checkout complet line")
    # )
    # checkouts_complet_line = graphene.List(CheckoutCompletLineType)

    def resolver_checkout_complet(self, _info, checkout_id):
        checkout_complet = CheckoutComplet.objects.filter(checkout_id=checkout_id).first()
        return checkout_complet

    def resolve_checkouts_complet(self, _info):
        checkouts_complet = CheckoutComplet.objects.all()
        return checkouts_complet

    # def resolve_checkout_complet_line(self, _info, id):
    #     checkout_complet_line = CheckoutCompletLine.objects.filter(id=id).first()
    #     return checkout_complet_line
    #
    # def resolve_checkouts_complet_line(self):
    #     checkouts_complet_lines = CheckoutCompletLine.objects.all()
    #     return checkouts_complet_lines


class CheckoutCompletMutations(graphene.ObjectType):
    checkout_complet_create = CheckoutCompletCreate.Field()
