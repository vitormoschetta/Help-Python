from operations import Operations

op = Operations()

def inputValues():
    x = input('Entre com o primeiro valor: ')
    y = input('Entre com o segundo valor: ') 
    return (x, y)  

def operationExecute(selected):
    if selected == '01': 
        (x, y) = inputValues()
        op.Soma(x, y)
    elif selected == '02':   
        (x, y) = inputValues()  
        op.Subtracao(x, y)
    elif selected == '03':  
        (x, y) = inputValues()
        op.Multiplicacao(x, y)
    elif selected == '04':   
        (x, y) = inputValues()
        op.Divisao(x, y)
    else:
        print('Opção inválida!')
        inity()

def operationSelect():    
    print('Escolha a operação que deseja realizar: ')
    print('01 - Soma')
    print('02 - Subtração')
    print('03 - Multiplicação')
    print('04 - Divisão')
    return input()    

def inity():
    selected = operationSelect()
    operationExecute(selected)

inity()




