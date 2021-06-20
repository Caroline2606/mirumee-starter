import pytest
from graphene_django.utils.testing import graphql_query
from ..product.models import Product, ProductVariant
from ..account.models import User
from ..checkout.models import Checkout, CheckoutLine
from decimal import Decimal

@pytest.fixture
def client_query(client):
    def func(*args, **kwargs):
        return graphql_query(*args, **kwargs, client=client)

    return func

@pytest.fixture
def my_product():
    product = Product.objects.create(
        name="Test Product",
        description="Product description",
        price=Decimal("10.00"),
        quantity=10.00
    )
    return product

@pytest.fixture
def variant(my_product):
    variant = ProductVariant.objects.create(
        product=my_product,
        name='My variant',
        sku='my-variant',
        price=Decimal("20.00"),
    )
    return variant

@pytest.fixture
def my_user():
    user = User.objects.create_user(
        email="Test.email@op.pl",
        password="Test password",
        first_name="Test first name",
        last_name="Test last name"
    )
    return user

@pytest.fixture
def my_checkout():
    checkout = Checkout.objects.create(
        userEmail="test userEmail",
        lines=[
            {"variant_id: 1", "quantity: 1"}
        ]
    )
    return checkout

@pytest.fixture
def checkout_line(my_checkout):
    checkout_line = CheckoutLine.objects.create(
        checkout=my_checkout,
        variantId=1,
        quantity=1
    )
    return checkout_line

