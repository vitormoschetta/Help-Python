from product import Product

class  ProductRepository:
    products = []
    
    def __init__(self):
        self.products = [
            Product('Product A', 5.99),
            Product('Product B', 99.50)
        ]

    def create(self, product):
        self.products.append(product)

    def getall(self):
        return self.products
        