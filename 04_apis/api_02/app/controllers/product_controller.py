from fastapi import APIRouter
from domain.entities.product import Product
from domain.requests.product_create import ProductCreate
from domain.requests.product_update import ProductUpdate
import infra.repositories.product_repository as repository

PRODUCT_CONTROLLER = APIRouter()


@PRODUCT_CONTROLLER.get("/load")
def load():
    repository.load()


@PRODUCT_CONTROLLER.get("/products")
def get_all():
    return repository.get_all()


@PRODUCT_CONTROLLER.get("/products/{id}")
def get_id(id: int):
    return repository.get_by_id(id)


@PRODUCT_CONTROLLER.post("/products")
def add(item: ProductCreate):
    product = Product(item.name, item.price, item.active)
    repository.add(product)


@PRODUCT_CONTROLLER.put("/products/{id}")
def update(id: str, item: ProductUpdate):
    if id != item.id:
        return 'Id inválido!'
    repository.update(item)


@PRODUCT_CONTROLLER.delete("/products/{id}")
def update(id: str):
    repository.delete(id)