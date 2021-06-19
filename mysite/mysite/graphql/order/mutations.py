import graphene

from .types import CheckoutCompletType
from ...order.models import CheckoutComplet


class CheckoutCompletCreateInput(graphene.InputObjectType):
    checkout_id = graphene.ID(required=True, description="ID of checkout")


class CheckoutCompletCreate(graphene.Mutation):
    checkout_complet = graphene.Field(CheckoutCompletType)

    class Arguments:
        input = CheckoutCompletCreateInput(required=True)
        checkout_id = graphene.ID(required=True)

    @classmethod
    def mutate(cls, root, info, input, checkout_id):

        checkout_complet = CheckoutComplet.objects.create(checkout_id=checkout_id)

        return CheckoutCompletCreate(checkout_complet=checkout_complet)


# class CheckoutCompletLineCreateInput(graphene.InputObjectType):
#     lines = graphene.List(CheckoutCompletCreateInput, required=True)
#
#
# class CheckoutCompletLineCreate(graphene.Mutation):
#     checkout_complet_line = graphene.Field(CheckoutCompletLineType)
#
#     class Arguments:
#         input = CheckoutCompletLineCreateInput(required=True)
#
#     @classmethod
#     def mutate(cls, root, info, input, checkout_id):
#         checkout_complet_line = CheckoutCompletLine.objects.create(checkout_id=checkout_id)
#
#         return CheckoutCompletLineCreate(checkout_complet_line=checkout_complet_line)
