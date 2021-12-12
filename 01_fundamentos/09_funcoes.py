def printValue(value):
    print(value)

def printValue(value: str):
    print(value)

def printValue(value: int):
    print(value)

def somar(num1: float, num2: float):    
    return num1 + num2

def somar(num1: float, num2: float) -> int:    
    return num1 + num2


printValue(5.99)

print(somar(5, 5.5))