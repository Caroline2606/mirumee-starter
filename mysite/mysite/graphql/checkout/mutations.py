import graphene

from .types import CheckoutType
from ...checkout.models import Checkout


class CheckoutCreateInput(graphene.InputObjectType):
    lines = graphene.String(required=True)
    user_email = graphene.String(required=True)

class CheckoutCreate(graphene.Mutation):
    checkout = graphene.Field(CheckoutType)

    class Arguments:
        input = CheckoutCreateInput(required=True)
        user_id = graphene.ID()

    @classmethod
    def clean_input(cls, data):
        return data

    @classmethod
    def mutate(cls, root, _info, input, user_id):
        cleaned_input = cls.clean_input(input)

        checkout = Checkout.objects.create(user_id=user_id, **cleaned_input)

        return CheckoutCreate(checkout=checkout)
