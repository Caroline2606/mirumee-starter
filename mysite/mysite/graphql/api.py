import graphene

from .product.schema import ProductQueries, ProductMutations
from .checkout.schema import CheckoutQueries, CheckoutMutations
from .account.authenticate import AuthenticateMutations



class Query(ProductQueries, CheckoutQueries):
    pass


class Mutations(ProductMutations, CheckoutMutations, AuthenticateMutations):
    pass


schema = graphene.Schema(query=Query, mutation=Mutations)