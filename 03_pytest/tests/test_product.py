import pytest
from models.product import Product

def test_price_is_greater_than_zero():
    product = Product('Product A', 0)
    separator = '. '
    assert product.is_invalid(), separator.join(product._notifications)

def test_name_not_empty():
    product = Product('Pro', 5)
    separator = '. '
    assert product.is_invalid(), separator.join(product._notifications)
     
def test_two_functions():
    product = Product('', 0)
    separator = '. '
    assert product.is_invalid(), separator.join(product._notifications)