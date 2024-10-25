lista: list = ["sapato", 39, 10.38, True]

# no dicionario

produto_1: dict = {
    "nome":"sapato",
    "quantidade":39,
    "preco":10.38,
    "disponibilidade":True
}

produto_2: dict = {
    "nome":"televisao",
    "quantidade":10,
    "preco":70,
    "disponibilidade":False
}

# é similar ao que vemos no excel: as colunas e os valores nas linhas
# https://docs.python.org/3/tutorial/datastructures.html
# seção 5.5
# metodos
# https://www.w3schools.com/python/python_ref_dictionary.asp

carrinho: list = []

carrinho.append(produto_1)
carrinho.append(produto_2)

print(carrinho)

import json

carrinho_json = json.dumps(carrinho)
print("json")
print(carrinho_json)

# dicionario de python é diferente do json java script
# no jaba bool é true e false
# no python é True e False