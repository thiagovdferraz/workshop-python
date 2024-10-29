# Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}

print("estoque original: " + str(estoque))

# list comprehension
estoque_sem_zero = {prod : qtde for prod, qtde in estoque.items() if qtde>0}

print(estoque_sem_zero)