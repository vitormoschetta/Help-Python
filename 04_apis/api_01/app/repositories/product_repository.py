from app.models.product import Product

_list = []


def load():
    x = 0
    while x < 5:
        prod = Product('Product ' + str(x), x)
        _list.append(prod)
        x = x + 1


def get_all():
    return _list


def get_by_id(id):
    index = 0
    while index < len(_list):
        if str(_list[index].id) == str(id):
            return _list[index]
        index += 1


def add(item: Product):
    _list.append(item)


def update(item: Product):
    index = 0
    while index < len(_list):
        if str(_list[index].id) == str(item.id):
            _list[index].name = item.name
            _list[index].price = item.price
            _list[index].active = item.active
        index += 1


def delete(id: str):
    index = 0
    while index < len(_list):
        if str(_list[index].id) == str(id):
            del _list[index]
        index += 1