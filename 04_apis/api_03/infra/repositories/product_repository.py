from domain.entities.product import Product

_list = []


def get_all():
    for x in range(5):
        prod = Product(x, 'Product ' + str(x), x)
        _list.append(prod)
    return _list


def get_by_id(id):
    _list = get_all()
    index = 0
    while index < len(_list):
        if str(_list[index].id) == id:
            return _list[index]
        index += 1


def add(item: Product):
    _list = get_all()
    _list.append(item)


