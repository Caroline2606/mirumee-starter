import graphene

from .product.schema import ProductQueries, ProductMutations
from .checkout.schema import CheckoutQueries, CheckoutMutations
from .account.authenticate import AuthenticateMutations
from .account.schema import UserQueries, UserMutations
from .order.schema import CheckoutCompletQueries, CheckoutCompletMutations


class Query(ProductQueries, CheckoutQueries, UserQueries, CheckoutCompletQueries):
    pass


class Mutations(ProductMutations, CheckoutMutations, AuthenticateMutations, UserMutations, CheckoutCompletMutations):
    pass


schema = graphene.Schema(query=Query, mutation=Mutations)
