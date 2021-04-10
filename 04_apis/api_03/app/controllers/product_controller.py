from fastapi import APIRouter
from domain.entities.product import Product
import infra.repositories.product_repository as repository

PRODUCT_CONTROLLER = APIRouter()


@PRODUCT_CONTROLLER.get("/product/")
def get_all():
    return repository.get_all()


@PRODUCT_CONTROLLER.get("/product/{id}")
def get_by_id(id):
    return repository.get_by_id(id)


