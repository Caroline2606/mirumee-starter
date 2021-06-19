import graphene

from ...account.models import User
from .types import UserType
from django.core.exceptions import ValidationError

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
    def clean_password(cls, password):
        for password in User:
            if password >= 8:
                return password
            if password < 8:
                raise ValidationError('Your password is too short')
        return password

    @classmethod
    def clean_name(cls, first_name, last_name):
        if not first_name[0].isupper() and last_name[0].isupper:
            raise SyntaxError('First letter in first_name and last_name is small')
        return first_name, last_name

    def clean_input(cls, data):
        cls.clean_password(input['password'])
        cls.clean_name(input['first_name']['last_name'])

        return data

    @classmethod
    def mutate(cls, root, _info, input):
        # cleaned_input = cls.clean_input(input)

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