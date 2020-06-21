import graphene
from graphene_django.types import DjangoObjectType
from .models import users

class UserType(DjangoObjectType):
    class Meta:
        model = users

class Query(graphene.ObjectType):
    allUsers = graphene.List(UserType)

    def resolve_allUsers(self, info, **kwargs):
        return users.objects.all()
