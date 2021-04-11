import uuid
from app.models.notifiable import Notifiable


class Product(Notifiable):
    def __init__(self, name, price, active=True):
        self.id = uuid.uuid4()
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
