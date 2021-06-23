from app.models.product import Product
from app.requests.product_create import ProductCreate
from app.requests.product_update import ProductUpdate
from app.responses.product_response import ProductResponse
from app.responses.generic_response import GenericResponse
import app.repositories.product_repository as repository
import uuid


def get_all():
    items = []
    for item in repository.get_all():
        product = ProductResponse(item.id, item.name, item.price)
        items.append(product)
    return items


def get(id: str):
    product = repository.get_by_id(id)
    if not product:
        return None
    return ProductResponse(product.id, product.name, product.price)


def add(item: ProductCreate):
    product = Product(uuid.uuid4(), item.name, item.price, item.active)
    repository.add(product)
    return GenericResponse(True, 'Cadastrado com sucesso!')


def update(item: ProductUpdate):
    repository.update(item)


def delete(id: str):
    repository.delete(id)
