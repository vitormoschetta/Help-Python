from operations import Operations

print('Escolha a operação que deseja realizar: ')
print('01 - Soma')
print('02 - Subtração')
print('03 - Multiplicação')
print('04 - Divisão')

operacao = input()
op = Operations()

if operacao == '01':
    x = input('Entre com o primeiro valor: ')
    y = input('Entre com o segundo valor: ')
    op.Soma(x, y)

if operacao == '02':
    x = input('Entre com o primeiro valor: ')
    y = input('Entre com o segundo valor: ')
    op.Subtracao(x, y)

if operacao == '03':
    x = input('Entre com o primeiro valor: ')
    y = input('Entre com o segundo valor: ')
    op.Multiplicacao(x, y)

if operacao == '04':
    x = input('Entre com o primeiro valor: ')
    y = input('Entre com o segundo valor: ')
    op.Divisao(x, y)
