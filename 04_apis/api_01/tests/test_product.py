import pytest
from app.models.product import Product
import uuid


def test_price_is_greater_than_zero():
    product = Product(uuid.uuid4(), 'Product A', 0)
    separator = '. '
    assert product.is_invalid, separator.join(product._notifications)


def test_name_not_empty_or_less_five_characters():
    product = Product(uuid.uuid4(), 'Pro', 5)
    separator = '. '
    assert product.is_invalid, separator.join(product._notifications)


def test_two_functions():
    product = Product(uuid.uuid4(), '', 0)
    separator = '. '
    assert product.is_invalid, separator.join(product._notifications)
