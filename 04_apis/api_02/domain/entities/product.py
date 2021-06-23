import uuid
from domain.entities.entity import Entity


class Product(Entity):
    def __init__(self, name, price, active=True):
        super(Product, self).__init__()
        self.name = name
        self.price = price
        self.active = active
        self.validate()

    def update(self, name, price):
        self.name = name
        self.price = price

    def validate(self):
        if len(self.name) < 5:
            self.add_notification('Nome do Produto deve conter no mínimo 5 caracteres!')
        if self.price <= 0:
            self.add_notification('Preço do Produto informado é inválido.')
