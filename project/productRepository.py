from product import Product

class  ProductRepository:
    def __init__(self):
        self.products = []

    def create(self, product):
        self.products.append(product)

    def getall(self):
        return self.products
        