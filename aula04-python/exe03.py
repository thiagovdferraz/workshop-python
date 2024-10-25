# crie um dict para armazenar informações de um livro
# incluindo titulo, autor e ano de publicacao

from typing import Dict, Any

livro_1: Dict[str, Any] = {
    "titulo": "game of thrones",
    "autor": "estagiario",
    "ano": 2005
}

livro_2: Dict[str, Any] = {
    "titulo": "game of thrones 2",
    "autor": "estagiario",
    "ano": 2007
}

print(livro_1)

print("")
print("print dicionario")
lista_elementos = livro_1.items()
for elemento in lista_elementos:
    print(elemento)

print("")
print("todos os livros")

lista_livros =[]

lista_livros.append(livro_1)
lista_livros.append(livro_2)

print(lista_livros)

print("")
print("dionarios dentro do dionario")
lista_livros_dict: dict ={
    "livro_01":{
    "titulo": "game of thrones",
    "autor": "estagiario",
    "ano": 2005
    },

    "livro_02":{
    "titulo": "game of thrones 2",
    "autor": "estagiario",
    "ano": 2007
    }
}

print("")
print("dicionario inteiro")
print(lista_livros_dict)
print("")
print("livro1")
print(lista_livros_dict["livro_01"])
print("")
print("livro1 - titulo")
print(lista_livros_dict["livro_01"]["titulo"])
