from fastapi import APIRouter
import infra.repositories.product_repository as ProductRepository

PRODUCT_CONTROLLER = APIRouter()


@PRODUCT_CONTROLLER.get("/product/")
def get_all():
    return ProductRepository.get_all()


@PRODUCT_CONTROLLER.get("/product/{id}")
def get_by_id(id):
    return ProductRepository.get_by_id(id)


