# tres formas de importar um módulo e/ou funcionalidades do módulo

# importando o módulo inteiro
import sys
print(sys.platform)

# importando apenas uma funcionalidade do módulo
from sys import platform
print(platform)

# dando um apelido (so):
from sys import platform as so
print(so)


import random

for i in range(10):
    print(random.randint(0,10))
    



