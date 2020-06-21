import graphene
from pythongraphql.schema import Query as userQuery

class Query(userQuery):
    pass

schema = graphene.Schema(query=Query)
