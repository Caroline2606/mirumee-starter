import graphene
from graphql_jwt.decorators import staff_member_required

from .types import UserType
from ...account.models import User
from .mutations import UserCreate, StaffCreate

class UserQueries(graphene.ObjectType):
    user = graphene.Field(
        UserType,
        email=graphene.Argument(graphene.String, description="Email of user.")
    )
    users = graphene.List(UserType)


    def resolve_user(self, _info, email):
        user = User.objects.filter(email=email).first()
        return user

    @staff_member_required
    def resolve_users(self, _info):
        users = User.objects.all()
        return users

class UserMutations(graphene.ObjectType):
    user_create = UserCreate.Field()
    staff_create = StaffCreate.Field()