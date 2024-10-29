# Implementação do algoritmo de ordenação por seleção
lista: int = [64, 34, 25, 12, 22, 11, 90]


def ordena_lista(numeros: list) -> list:
    nova_lista_numeros = numeros.copy()

    for i in range(len(nova_lista_numeros)):
        for j in range(i+1, len(nova_lista_numeros)):
            if nova_lista_numeros[i] > nova_lista_numeros[j]:
                nova_lista_numeros[i], nova_lista_numeros[j] = nova_lista_numeros[j], nova_lista_numeros[i]
    return nova_lista_numeros

nova_lista = ordena_lista(lista)

# Ordenando a lista
print("Lista ordenada com função personalizada:", nova_lista)

print("")
print("Ordenação com a função sorted")
print(sorted(lista))
print("")
print("Ordenação com a método sort")
lista.sort()
print(lista)