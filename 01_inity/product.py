class Product:
    def __init__(self, id, name):
        self.id = id
        self.name = name
                      


lista = []
prodA = {'id': '01', 'name': 'prod A'}
prodB = {'id': '02', 'name': 'prod B'}
prodC = Product('03', 'prod C')

lista.append(prodA)
lista.append(prodB)
lista.append(prodC)

print(lista[1].id)

