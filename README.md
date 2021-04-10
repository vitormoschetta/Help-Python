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

<br>




