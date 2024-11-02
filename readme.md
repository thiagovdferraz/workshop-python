# Bootcamp Python

## Aula 01
Introdução, git e vscode: python do zero

## Aula 02
TypeError, Type Check, Type Conversion, try-except e if

* operacoes logicas: +, -, *, //, %, **, /
* strings, booleanos, float
* tipos de erro que o python nos mostra
* como lidar com erros atraves do try e except
* converter variaveis de um tipo para outro: int para str
* tratativas de erros
* condicional if, elif

## Aula 03
Debug, IF, FOR, While, Listas e Dicionários

* Debug: executar o código linha a linha para encontrar possíveis bugs
* exemplo com while e for
* exemplo com condicinal if
* entender dicionários: [Ver aula dicionários](https://www.youtube.com/watch?v=ZWj8o692qGY)
* entender listas

## Aula 04
Typing, listas e dicionários

[Teoria Jornada](https://github.com/lvgalvao/data-engineering-roadmap/tree/main/Bootcamp%20-%20Python%20para%20dados/aula04)

* tipos complexos: listas e dicionários
* type hint: ajuda a tornar o código mais legível e seguro. Ele não converte o tipo da variável (faz cast).
* dicionários vs dataframes vs tabelas vs excel

## Aula 05

Desafio para ler 1 Bilhão de linhas via CSV - Fork Projeto Luciano Galvão
* teste via biblioteca python
* teste com pandas
* teste com polars
* teste com dask
* teste com duckdb

## Aula 06

Dicas de boas práticas
* pep 8
* criar ambiente com poetry e verificar se o código está dentro das conformidades de boa escrita

```python
pyenv local 3.12.1
poetry init
poetry env use 3.12.1
poetry shell
poetry add flake8
poetry run flake8 arquivo.py
```

O **flake8** dá dicas de como melhorar o código. pode ser muito trabalhoso.

O **black** já faz o trabalho pra gente. Incompátivel com python 3.12.5.

```python
poetry add black
poetry run black arquivo.py
```

O **blue** é parecido com o **black**.

```python
poetry remove flak8
poetry remove black
poetry add blue
poetry run blue .
poetry run flake8
```

Outra opção é utilizar o **isort**.

```python
poetry add isort
poetry run isort file.py
```

No arquivo do `pyproject` é necessário incluir o código abaixo para excluir possíveis conflitos entre black, isort e flake8.

```
[tool.isort]
profile = "black"
```

Incluir um comando para executar os três sem conflitos.
```
poetry add taskipy
``` 

Incluir no `pyproject`
```
[tool.taskipy.tasks]
format = """
isort file.py
black file.py
flake8 file.py
"""
```

Depois executar `poetry run task format`

Para assegurar que todos do time rode essas correções nos códigos, precisamos configurar uma "trava".
Aqui entra o `pre-commit`.

https://pre-commit.com/

https://pre-commit.com/hooks.html

```
poetry add pre-commit
``` 

Configura o arquivo `.pre-commit-config.yaml` e rode 
```
poetry run pre-commit install
git add .pre-commit-config.yaml
``` 

Agora toda vez que comitar um código, ele passará por uma série de testes.