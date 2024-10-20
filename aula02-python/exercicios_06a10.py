# Números de Ponto Flutuante (float)

# Escreva um programa que receba dois números flutuantes e realize sua adição.
# number_1 = float(input("entre com um numero: "))
# number_2 = float(input("entre com um numero: "))

# add = number_1 + number_2
# print(f"a soma e: {add}")

# Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# number_1 = float(input("entre com um numero: "))
# number_2 = float(input("entre com um numero: "))

# media = (number_1 + number_2) / 2
# print(f"a media e: {media}")

# Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# base = float(input("entre com um numero: "))
# expoente = float(input("entre com um numero que deseja elevar: "))

# potencia = base ** expoente
# print(f"o resultado de {base}^{expoente} e: {potencia}")

# Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# temp_celsius = float(input("entre com a temperatura em celsius: "))

# fahrenheit = temp_celsius *1.8 + 32
# print(f"{temp_celsius}º celsius em fahrenheit e: {fahrenheit}º")

# Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
import math
num_pi = math.pi
raio = float(input("entre com o raio do circulo: "))

area = num_pi * raio **2
print(f"a area do circulo e: {round(area,2)}")