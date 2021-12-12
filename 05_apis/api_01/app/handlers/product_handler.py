from app.models.product import Product
from app.requests.product_create import ProductCreate
from app.requests.product_update import ProductUpdate
from app.responses.product_response import ProductResponse
from app.responses.generic_response import GenericResponse
import app.repositories.product_repository as repository
import app.helpers.concatenate_list as concatenate
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
    if product.is_invalid:
        return GenericResponse(False, concatenate.build(product.notifications))
    repository.add(product)
    return GenericResponse(True, 'Cadastrado com sucesso!')


def update(item: ProductUpdate):
    product = repository.get_by_id(item.id)
    if not product:
        return GenericResponse(False, 'Produto não encontrado!')
    product.update(item.name, item.price)
    if product.is_invalid:
        return GenericResponse(False, concatenate.build(product.notifications))
    repository.update(item)
    return GenericResponse(True, 'Atualizado com sucesso!')


def delete(id: str):
    product = repository.get_by_id(id)
    if not product:
        return GenericResponse(False, 'Produto não encontrado!')
    repository.delete(id)
    return GenericResponse(True, 'Excluído com sucesso!')
