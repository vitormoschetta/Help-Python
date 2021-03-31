from product import Product

prod = Product('Product A', 5.5)

if len(prod._notifications) > 0:
    print(prod._notifications[0])

b = 150
expressao = 100 > b
mensagem  = "100 deve ser maior que 'b'"
assert expressao, mensagem
