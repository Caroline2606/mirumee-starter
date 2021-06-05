import graphene
from graphql_jwt.decorators import staff_member_required

from .types import UserType, StaffType
from ...account.models import User, UserManager
from .mutations import UserCreate, StaffCreate

class UserQueries(graphene.ObjectType):
    user = graphene.Field(
        UserType,
        id=graphene.Argument(graphene.ID, description="ID of user.")
    )
    users = graphene.List(UserType)
    superuser = graphene.Field(
        StaffType,
        id=graphene.Argument(graphene.ID, description="ID of superuser.")
    )


    def resolve_user(self, _info, email):
        user = User.objects.filter(email=email).first()
        return user

    @staff_member_required
    def resolve_users(self, info):
        users = User.objects.all()
        return users

    def resolve_superuser(self, _info, id):
        superuser = UserManager.objects.filter(id=id).first()
        return superuser

class UserMutations(graphene.ObjectType):
    user_create = UserCreate.Field()
    superuser_create = StaffCreate.Field()