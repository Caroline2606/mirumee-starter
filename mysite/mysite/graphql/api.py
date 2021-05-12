import graphene

from ..graphql.product.schema import ProductQueries, ProductMutations

class Query(ProductQueries):
    pass

schema = graphene.Schema(query=Query, mutation=ProductMutations)