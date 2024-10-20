nome = "thiago"
print(type(nome))

# upper()
# lower()
# strip(): remover espaços em branco
# split(sep): divide string numa lista
# +

# string = ' thiago@123.com'
# print(string.upper())
# print(string.lower())
# print(string.strip())
# print(string.split("@"))

# # Exercícios
# # exe04

# print("exercicio 04")
# numero1 = int(input("inserir um numero inteiro: "))
# numero2 = int(input("inserir um numero inteiro: "))

# resultado = numero1 // numero2

# print(resultado)

# Exercícios
# exe10

# print("exercicio 10? area do circulo")
# raio_circulo = float(input("inserir o raio: "))

# import math
# area = math.pi * raio_circulo ** 2

# print("area do circulo e: ")
# print(f"{area:.2f}")

# exe 15

# data = input("insira uma data no formato dd/mm/aaaa: ")
data = "10/02/1990"
lista_dia_mes_ano = data.split("/")
print(lista_dia_mes_ano)
print(f"o elemento 1 e o: {lista_dia_mes_ano[0]}")
print(f"o elemento 2 e o: {lista_dia_mes_ano[1]}")
print(f"o elemento 3 e o: {lista_dia_mes_ano[2]}")