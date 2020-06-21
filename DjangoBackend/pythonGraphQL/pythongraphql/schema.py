import graphene
from graphene_django.types import DjangoObjectType
from .models import users
from datetime import datetime

class UserType(DjangoObjectType):
    class Meta:
        model = users

class Query(graphene.ObjectType):
    allUsers = graphene.List(UserType)
    userById = graphene.Field(UserType, id=graphene.ID())

    def resolve_allUsers(self, info, **kwargs):
        return users.objects.all()

    def resolve_userById(self, info, id, **kwargs):
        return users.objects.get(pk=id)

# mutation for adding a user
class AddUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)
        dateOfBirth = graphene.Date(required=True)

    user = graphene.Field(UserType)

    def mutate(self, info, username, password, email, dateOfBirth):
        user = users(username=username, password=password, email=email, dateCreated = datetime.now(), dateOfBirth=dateOfBirth)
        user.save()
        return AddUser(user=user)

# mutation for updating a user 
class UpdateUser(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        username = graphene.String()
        password = graphene.String()
        email = graphene.String()
        dateOfBirth = graphene.Date()

    user = graphene.Field(UserType)

    def mutate(self, info, id, username=None, password=None, email=None, dateOfBirth=None):
        user = users.objects.get(pk=id)
        if username is not None: user.username = username 
        if password is not None: user.password = password
        if email is not None: user.email = email
        if dateOfBirth is not None: user.dateOfBirth = dateOfBirth
        user.save()
        return UpdateUser(user=user)

# mutation for deletinga user
class DeleteUser(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    user = graphene.Field(UserType)

    def mutate(self, info, id):
        user = users.objects.get(pk=id)
        user.delete()
        return DeleteUser(user=user)

class Mutations(graphene.ObjectType):
    addUser = AddUser.Field()
    updateUser = UpdateUser.Field()
    deleteUser = DeleteUser.Field()
        