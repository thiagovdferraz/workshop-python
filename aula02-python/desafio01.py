# solicitar nome do usuário

nome = input("Digite seu nome: ")

if nome.isdigit():
    print("pode ter numeros em seu nome!")
    exit()
elif len(nome):
    print("voce nao digitou nada")
    exit()
elif nome.isspace:
    print("voce digitou somente espaco")
    exit()

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