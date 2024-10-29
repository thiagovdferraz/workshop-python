# Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.

texto = "engenharia de dados"

freq = {}

for keys in texto:
    freq[keys] = freq.get(keys, 0) + 1

print('metodo 1')
print(str(freq))

# metodo 2

frequencia = {}

for letra in texto:
    if letra in frequencia:
        frequencia[letra] += 1
    else:
        frequencia[letra] = 1

print('metodo 2')
print(frequencia)
