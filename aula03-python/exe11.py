# 11. Leitura de Dados até Flag

# Objetivo: Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

dados = []
entrada = ""
while entrada.lower() != "sair":
    entrada = input("Digite um valor (ou 'sair' para terminar): ")
    if entrada.lower() != "sair":
        print('continua')