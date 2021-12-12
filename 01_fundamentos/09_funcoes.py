# funcao simples
def printValue(value):
    print(value)

# funcao com argumento tipado
def printValue(value: str):
    print(value)

# funcao com argumento tipado e retorno não tipado
def somar(num1: float, num2: float):    
    return num1 + num2

# funcao com argumento e retorno tipados
def somar(num1: float, num2: float) -> float:    
    return num1 + num2


printValue(5.99)

result = somar(5, 5.5)
print(result)


# Callback
def calcular(num1, num2, operacao):
    result = operacao(num1, num2)
    print(result)   

calcular(5, 3, somar)