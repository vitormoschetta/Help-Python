# importando o módulos
from modulo_xpto import func_print, func_calc
func_print.printValue("123")
result = func_calc.somar(5, 2)
print(result)

# importando apenas uma funcao de um módulo especifico
from modulo_xpto.func_print import printValue
printValue(1989)

# atribuindo apelido
from modulo_xpto.func_print import printValue as mostrar
mostrar(2001)


    



