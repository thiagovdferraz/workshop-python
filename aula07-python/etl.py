# * Ler o arquivo CSV e carregar os dados.
# * Processar os dados em um dicionário, onde a chave é a categoria, e o valor é uma lista de dicionários, cada um contendo informações do produto (Produto, Quantidade, Venda).
# * Filtrar somente produtos que foram entregues

import csv

path_arquivo = "vendas.csv"

def ler_csv(nome_do_arquivo_csv) -> list[dict]:
    """
    Função que lê uym arquivo csv e retorna uma lista
    de dicionários.
    """
    lista = []
    with open("vendas.csv", mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista

# vendas_base: list[dict]

# vendas_base = ler_csv(path_arquivo)
# print(vendas_base)


def filtrar_produtos_entregues(lista: list[dict]) -> list[dict]:
    """
    Função que filtra produtos entregues.
    """
    lista_prod_filtrados = []
    for produtos in lista:
        if produtos.get("Entregue") == "True":
            lista_prod_filtrados.append(produtos)
    return lista_prod_filtrados

def somar_valores_dos_produtos(lista_prod_filtrados: list[dict]) -> int:
    """
    Soma dos produtos entregues.
    """
    valor_total = 0
    for produtos in lista_prod_filtrados:
        valor_total += int(produtos.get("Venda"))
    return valor_total