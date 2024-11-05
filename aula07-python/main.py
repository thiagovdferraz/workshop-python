from etl import ler_csv, filtrar_produtos_entregues, somar_valores_dos_produtos

path_arquivo = "vendas.csv"

lista_produtos = ler_csv(path_arquivo)
produtos_entregues = filtrar_produtos_entregues(lista_produtos)
valor_prod_entregue = somar_valores_dos_produtos(produtos_entregues)
print(produtos_entregues)
print(f"Total de vendas, somente produtos entregues: {valor_prod_entregue}")