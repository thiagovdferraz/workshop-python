# definindo função para somar dois numeros

def soma(valor_1: float, valor_2:float) -> float:
    """
    Uma função simples que retorna a soma de dois números float.
    """
    resultado_soma = valor_1 + valor_2
    return resultado_soma

valor_1 = 10.10
valor_2 = 2.30
resultado = soma(valor_1, valor_2)

print(f"Soma dos valores: {resultado}")