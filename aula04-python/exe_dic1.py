# Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

produtos = [
    {"id": 1, "nome": "Teclado", "preço": 100},
    {"id": 2, "nome": "Mouse", "preço": 80},
    {"id": 3, "nome": "Monitor", "preço": 300}
]

# atualizar preco do produto copm id2 para 90

for prod in produtos:
    if prod['id'] == 2:
        prod['preço'] = 90

print(produtos)
