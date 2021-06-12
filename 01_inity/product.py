class Product:
    def __init__(self, cod, name):
        self.cod = cod
        self.name = name


lista = []

for i in [0, 1, 2, 3, 4]:
    prod = Product(i, 'prod'+str(i))
    lista.append(prod)

for product in lista:
    print(product.name)

