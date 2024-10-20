# exemplo01
# try: # tente isso
#     print("exercicio 04")
#     numero1 = int(input("inserir um numero inteiro: "))
#     numero2 = int(input("inserir um numero inteiro: "))
#     resultado = numero1 // numero2
#     print(resultado)
#     # se der errado faz isso
# except ZeroDivisionError:
#     print("erro de divisao por zero")

# https://docs.python.org/3/tutorial/errors.html

# exemplo 02
# Exemplo que causa TypeError
# try:
#     resultado = len(5)
# except TypeError as e:
#     print(e)  # Imprime a mensagem de erro
# else:
#     print("tudo ocorreu bem")
# finally:
#     print("o importante e tentar")

# exemplo 03
# instance

numero = int(input("insira um numero: "))
if isinstance(numero, int):
    print("A variável é um inteiro.")
else:
    print("A variável não é um inteiro.")