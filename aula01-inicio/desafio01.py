# solicitar nome do usuário

nome = input("Digite seu nome: ")

# entra com seu salario 
salario = float(input("Digite seu salário: "))

# qual o bonus
bonus = float(input("Digite a porcentagem do bônus: "))/100

# valor do bonus final
constante_bonus = 1000
valor_final = round(constante_bonus + salario*bonus,2)

# imprima o calculo
print(f"KPI: {constante_bonus} + salário*bônus")
print("")

# valores
print(f"{nome}, o bônus final de R$ {valor_final}.")