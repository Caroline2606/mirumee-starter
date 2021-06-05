import graphene
from graphql_jwt.decorators import superuser_required

from ...account.models import User, UserManager
from .types import UserType, StaffType

class UserCreateInput(graphene.InputObjectType):
    email = graphene.String()
    first_name = graphene.String()
    last_name = graphene.String()

class UserCreate(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        input = UserCreateInput(required=True)

    @classmethod
    @superuser_required
    def mutate(cls, root, _info, input):
        user = User.objects.create(**input)

        return UserCreate(user=user)


class StaffCreateInput(graphene.InputObjectType):
    email = graphene.String()
    password = graphene.String()

class StaffCreate(graphene.Mutation):
    superuser = graphene.Field(StaffType)

    class Arguments:
        input = StaffCreateInput(required=True)

    @classmethod
    def mutate(cls, root, _info, input):
        superuser = UserManager.objects.create_superuser(**input)

        return StaffCreate(superuser=superuser)