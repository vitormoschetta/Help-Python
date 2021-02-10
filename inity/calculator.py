def Result(result):
    print('Resultado: ' + str(result))

def Soma(x, y):
    soma = int(x) + int(y)
    Result(soma)

def Subtracao(x, y):
    sub = int(x) - int(y)
    Result(sub)



print('Escolha a operação que deseja realizar: ')
print('01 - Soma')
print('02 - Subtracao')

operacao = input()

if operacao == '01':
    x = input('Entre com o primeiro valor: ')
    y = input('Entre com o segundo valor: ')
    Soma(x, y)

if operacao == '02':
    x = input('Entre com o valor maior: ')
    y = input('Entre com o valor menor: ')
    Subtracao(x, y)


    
