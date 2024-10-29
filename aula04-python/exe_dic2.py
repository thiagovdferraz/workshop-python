# Objetivo: Dados dois dicionários, fundi-los em um único dicionário.

dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"c": 3, "d": 4}

# Python unpacking operator
#dicionario_fundido = {**dicionario1, **dicionario2}

#print(dicionario_fundido)

# Python update() – The Best Way
# dicionario2.update(dicionario1)
# print(dicionario2)

#Python Merge Dictionaries Using | in Python 3.9
d3 = dicionario2 | dicionario1
print(d3)