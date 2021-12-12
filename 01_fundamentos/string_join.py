
############ Usando objetos:
class Product:
    def __init__(self, cod, name):
        self.cod = cod
        self.name = name


lista = []

for i in range(0, 5):
    product = Product(i, 'Product ' + str(i))
    lista.append(product)

def return_name():
    listaName = []
    for product in lista:
        listaName.append(product.name)
    return listaName


separetor = ' | '

print(separetor.join(return_name()))