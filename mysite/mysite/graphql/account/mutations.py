import graphene

from ...account.models import User
from .types import UserType

class UserCreateInput(graphene.InputObjectType):
    email = graphene.String()
    password = graphene.String()
    first_name = graphene.String()
    last_name = graphene.String()

class UserCreate(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        input = UserCreateInput(required=True)

    @classmethod
    def mutate(cls, root, _info, input):
        user = User.objects.create_user(**input)

        return UserCreate(user=user)


class StaffCreate(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        input = UserCreateInput(required=True)

    @classmethod
    def mutate(cls, root, _info, input):
        staff = User.objects.create_user(**input, is_staff=True)

        return StaffCreate(user=staff)