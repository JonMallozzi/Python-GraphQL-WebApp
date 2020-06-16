import graphene
import json
from datetime import date, datetime

class User(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    password = graphene.String()
    email = graphene.String()
    dateCreated = graphene.DateTime()
    dateOfBirth = graphene.DateTime()

class Query(graphene.ObjectType):
    users = graphene.List(User)

    def resolve_users(self, info):
        return [
            User(
                    id=1, 
                    username='Aerith', 
                    password='badPassword', 
                    email='Aerith@company.com', 
                    dateCreated=datetime.now(), 
                    dateOfBirth=date(1985,2,7)
                )
        ]

class CreateUser(graphene.Mutation):

    class Arguments:
        username = graphene.String()
        password = graphene.String()
        email = graphene.String()
        dateOfBirth = graphene.Date()

    user = graphene.Field(User)

    def mutate(self, info, username, password, email, dateOfBirth):
        user = User(username=username, password=password, email=email, dateOfBirth=dateOfBirth)
        return CreateUser(user=user)

class Mutations(graphene.ObjectType):
    createUser = CreateUser.Field()

schema = graphene.Schema(query=Query, mutation=Mutations)

result = schema.execute(
    '''
       mutation createUser {
           createUser(
               username: "Aerith",
               password: "badPassword",
               email:"A@gmail.com",
               dateOfBirth:"1989-02-08"
              ){
               user {
                username
                password
                email
                dateOfBirth
               }
           }
        }
    '''
)

items = dict(result.data.items())
print(json.dumps(items, indent=4))