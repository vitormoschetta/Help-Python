import uuid

class  Product:
    def __init__(self, name, price):
        self.id = uuid.uuid4()
        self.name = name
        self.price = price
        