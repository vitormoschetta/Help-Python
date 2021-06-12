class Product:
    def __init__(self, cod, name):
        self.cod = cod
        self.name = name


lista = []

for i in [0, 1, 2, 3, 4]:
    prod = Product(i, 'prod'+str(i))
    lista.append(prod)

i = 0
while i < len(lista):
    print(lista[i].name)
    i = i + 1

