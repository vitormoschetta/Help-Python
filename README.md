## Ambiente Python

#### versão
Imprime a versão _setada_ como _default_:
```
python -V
``` 

Podem existir outras versões instaladas:
```
python3.6 -V
``` 
```
python3.7 -V
``` 

<br>

#### Path 
Imprime o diretório de instalacao do Python (versão _default_):
```
which python
``` 
A saída disso seria algo como:
```
/usr/bin/python
```

Diretório de outras versões:
```
which python3.7
``` 

Saber pra onde a versão _default_ está apontando, em termos de _path_:
```
ls -ltrh <path>
``` 
Substituir o `<path>` acima pelo caminho gerado nos comandos anteriores.


<br>

#### Conflito de Versões de Pacotes - venv

Todos os pacotes Python são instalados na máquina de desenvolvimento local. Não é possível ter versões diferentes de um mesmo pacote instalados na mesma máquina. Logo terei problema caso esteja trabalhando em projetos diferentes que implementam diferentes versões de um mesmo pacote. 

Solução: `Virtual Env`
Virtual Env como um container criado em cada projeto para gerenciar os pacotes utilizados por este. Isolando os pacotes utilizados em cada projeto.

A IDE PyCharm (Gratuita) já cria esse ambiente ao criar um novo projeto Python.

Se tentarmos executar um projeto python fora da _venv_ provavelmente tomaremos erro por falta de módulos instalados. Eles foram na verdade instalados na _venv_ vinculada ao projeto mas não na máquina local.

Além de acessar a _venv_ através da ide PyCharm, podemos acessá-la via linha de comando:
```
source venv/bin/activate
```
<br>


#### Virtual Env in VS Code
```
sudo apt install virtualenv
```
Na pasta do projeto executar:
```
virtualenv --python=python venv
```
Para entrar no modo virtual env:
```
source venv/bin/activate
```

<br>

#### Python Package 
Para que um determinado arquivo python seja **importável** é necessário que ele seje um Python Package, para isso basta adicionar um arquivo **__init__.py** no diretório.




#### Python Singleton

A melhor e mais simples maneira de assegurar única instância de um determinado módulo é não usando classes. Módulos com propriedades e métodos apenas. 