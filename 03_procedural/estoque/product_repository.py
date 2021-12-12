from product import Product

products = [ 
    Product(1, "product a"),
    Product(2, "product b")
]


def getAll():
    return products

def getById(id):
   for product in products:
        if product.id == id:
            return product

def add(item):
    products.append(item)

def update(item):
    for product in products:
        if product.id == item.id:
            product.name = item.name

def delete(id):
    for product in products:
        if product.id == id:
            products.remove(product)