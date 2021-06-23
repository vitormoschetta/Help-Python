from fastapi import APIRouter
from app.requests.product_create import ProductCreate
from app.requests.product_update import ProductUpdate
import app.handlers.product_handler as handler


PRODUCT_CONTROLLER = APIRouter()


@PRODUCT_CONTROLLER.get("/products")
def get_all():
    items = handler.get_all()
    return items


@PRODUCT_CONTROLLER.get("/products/{id}")
def get_id(id: str):
    return handler.get(id)


@PRODUCT_CONTROLLER.post("/products")
def add(item: ProductCreate):
    return handler.add(item)


@PRODUCT_CONTROLLER.put("/products/{id}")
def update(id: str, item: ProductUpdate):
    if id != item.id:
        return 'Id inválido!'
    handler.update(item)


@PRODUCT_CONTROLLER.delete("/products/{id}")
def update(id: str):
    handler.delete(id)
