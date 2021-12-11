## Virtual Env

Quando estamos desenvolvendo diversos projetos em Python, é comum utilizarmos diferentes versões de uma mesma biblioteca entre este projetos. Por exemplo, imagine que estamos desenvolvendo o **projeto x** com a biblioteca `mysqlclient` em sua `versão 1.0` e o **projeto y** com a mesma biblioteca, porém na `versão 2.0`. Como faríamos para gerenciar estas dependências e o sistema operacional saber qual versão correta executar quando estivermos em cada projeto?

Esta é uma tarefa um tanto quanto complexa para o SO gerenciar, podendo acarretar em conflitos entre as versões e causar muita dor de cabeça. Sendo assim, o mais comum é utilizarmos diferentes ambentes virtuais, chamados de **virtualenvs**, um para cada projeto.

Basicamente, um `ambiente virtual` empacota todas as dependências que um projeto precisa e armazena em um diretório, fazendo com que nenhum pacote seja instalado diretamente no sistema operacional. Sendo assim, cada projeto pode possuir seu próprio ambiente e, consequentemente, suas bibliotecas em versões específicas.


### Instalar virtualenv

```
sudo apt install virtualenv
```


### Habilitar virtualenv

##### Adicionar virtualenv ao local:
```
virtualenv --python=python3.8 venv
```

##### Ativar virtualenv no terminal:
```
source venv/bin/activate
```
