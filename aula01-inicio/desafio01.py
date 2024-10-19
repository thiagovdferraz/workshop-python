# solicitar nome do usuário

nome = input("Digite seu nome: ")

# entra com seu salario 
salario = float(input("Digite seu salário: "))

# qual o bonus
bonus = float(input("Digite a porcentagem do bônus: "))/100

# valor do bonus final
valor_final = round(1000 + salario*bonus,2)

# imprima o calculo
print("KPI: 1000 + salário*bônus")
print("")

# valores
print(f"{nome}, o bônus final de R$ {valor_final}.")