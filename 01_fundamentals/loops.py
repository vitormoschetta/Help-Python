class Product:
    def __init__(self, cod, name):
        self.cod = cod
        self.name = name


listaA = []
listaB = []

# Gerar conteúdo das listas (duas formas):
for i in [0, 1, 2, 3, 4]:
    product = Product(i, 'prod'+str(i))
    listaA.append(product)

for i in range(0, 5):
    product = Product(i, 'prod'+str(i))
    listaB.append(product)


# Percorrer listas imprimindo name of product (duas formas):
for product in listaA:
    print(product.name)

i = 0
while i < len(listaB):
  print(listaA[i].name)
  i += 1




