# tres formas de importar um módulo e/ou funcionalidades do módulo

import sys
print(sys.platform)

from sys import platform
print(platform)

from sys import platform as so
print(so)



import random

for i in range(10):
    print(random.randint(0,10))
    



# Módulo de conexao com DB MySql
# Não vem nativamente, precisa instalar. Usar o seguinte comando:
# pip install pymysql
import pymysql    



