from fastapi import APIRouter
import uuid

PRODUCT_CONTROLLER = APIRouter()


class Notifiable:
    _notifications = []

    def add_notification(self, message):
        self._notifications.append(message)

    def is_valid(self):
        if len(self._notifications) > 0:
            return False
        else:
            return True

    def is_invalid(self):
        return not self.is_valid()


class Product(Notifiable):
    def __init__(self, name, price):
        self.id = uuid.uuid4()
        self.name = name
        self.price = price
        self.validate()

    def update(self, name, price):
        self.name = name
        self.price = price

    def validate(self):
        if len(self.name) < 5:
            self.add_notification('Nome do Produto deve conter no mínimo 5 caracteres!')
        if self.price <= 0:
            self.add_notification('Preço do Produto informado é inválido.')


# Response for write
class ProductResponse:
    def __init__(self, success: bool, data: Product):
        self.success = success
        self.data = data


def get_all_product():
    result = []
    for x in range(5):
        prod = Product('Product '+ str(x), x)
        result.append(prod)
    return result


@PRODUCT_CONTROLLER.get("/product/")
def get_all():
    return get_all_product()




