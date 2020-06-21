import graphene
from pythongraphql.schema import Query as userQuery
from pythongraphql.schema import Mutations as userMutations

class Query(userQuery):
    pass

schema = graphene.Schema(query=Query, mutation=userMutations)
