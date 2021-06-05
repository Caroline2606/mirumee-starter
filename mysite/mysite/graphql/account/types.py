from graphene_django import DjangoObjectType
from ...account.models import User, UserManager

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'

class StaffType(DjangoObjectType):
    class Meta:
        model = UserManager
        fields = '__all__'
