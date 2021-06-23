from app.models.product import Product

product_list = [
    Product('a5508eb2-1502-471d-af3d-6f916e5de3fd', 'Product A', 5.50),
    Product('e48cd52a-1328-4b65-aef3-41c81d3dbdff', 'Product B', 1.50),
    Product('0f1c334e-2adc-4177-be22-ba647c9388d1', 'Product C', 8.00),
    Product('8415d581-715f-4d21-9234-2ded2a530a06', 'Product D', 2.80),
]


def get_all():
    return product_list


def get_by_id(id):
    for product in product_list:
        if product.id == id:
            return product
    return None


def add(item: Product):
    product_list.append(item)


def update(item: Product):
    for product in product_list:
        if product.id == item.id:
            product.update(item.name, item.price)
            return


def delete(id: str):
    index = 0
    while index < len(product_list):
        if str(product_list[index].id) == str(id):
            del product_list[index]
        index += 1