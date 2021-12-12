from product import Product

products = [
    Product(1, "product a"),
    Product(2, "product b")
]


def getAll():
    return products


def getById(id: int):
    for product in products:
        if product.id == id:
            return product


def add(name: str):
    id = len(products) + 1
    product = Product(id, name)
    products.append(product)


def update(item):
    for product in products:
        if product.id == item.id:
            product.name = item.name
            return


def delete(item) -> bool:
    for product in products:
        if product == item:
            products.remove(product)
            return True
