# https://docs.python.org/3/tutorial/datastructures.html

produto_1: str = "sapato"
produto_2: str = "camiseta"
produto_3: str = "videogame"

produtos: list = []

# inclui itens na lista
produtos.append(produto_1)
produtos.append(produto_2)
produtos.append(produto_3)

print(produtos)

# remover itens
produtos.pop() # tira o ultimo produto que entrou

print(produtos)

produtos.remove(produto_2) # tira o item especificado

print(produtos)

print("")
print("exemplo 2")

numeros = []
numeros.extend(range(0,5))
print(numeros)