############### Lista de tipos primitivos:

listaA = ['a', 'b', 'c']
listaA.append('d')

for item in listaA:
    print(item)



############### Lista de objetos

### Objeto
class Product:
    def __init__(self, cod, name):
        self.cod = cod
        self.name = name


# lista instanciada já com valor:
listaB = [Product(1, 'Product A'), Product(2, 'Product B')]

# novo objeto add em tempo de instanciacao na lista
listaB.append(Product(3, 'Product C'))

# instancia do objeto product
product = Product(4, 'Product D')

# add objeto instanciado
listaB.append((product))

for product in listaB:
    print(product.name)




# Uma outra forma de percorrer listas de tipos primitivos:

print(listaA[0])        # print do primeiro elemento

print(listaA[0:])       # print de todos os elementos

print(listaA[1:])       # print do segundo elemento até o final

print(listaA[:-1])      # print primeiro elemento até um antes do final
