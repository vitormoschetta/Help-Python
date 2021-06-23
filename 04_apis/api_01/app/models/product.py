from app.models.entity import Entity


class Product(Entity):
    def __init__(self, id, name, price, active=True):
        super(Product, self).__init__(id)
        self.__name = name
        self.__price = price
        self.__active = active
        self.validate()

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def active(self):
        return self.__active

    def update(self, name, price):
        self.__name = name
        self.__price = price
        self.validate()

    def validate(self):
        if len(self.name) < 5:
            self.add_notification('Nome do Produto deve conter no mínimo 5 caracteres!')
        if self.price <= 0:
            self.notifications.append('Preço do Produto informado é inválido.')
