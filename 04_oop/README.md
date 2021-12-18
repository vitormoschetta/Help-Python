### __new__ ou __init__

A maioria das linguagens de programação orientadas a objetos, como Java, C ++, C # .. etc, têm o conceito de um construtor, um método especial que cria e inicializa o objeto quando ele é criado. Python é um pouco diferente; ele tem um **construtor** e um **inicializador**.

A função construtora em python é chamada `__new__`e `__init__` é a função inicializadora.

`__new__`é a primeira etapa da criação da instância. Ele é chamado primeiro e é responsável por retornar uma nova instância de sua classe.

Em contraste, `__init__` não retorna nada; ele só é responsável por inicializar a instância após sua criação. 
