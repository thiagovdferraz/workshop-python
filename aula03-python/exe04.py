# Exercício 4: Validação de Dados de Entrada

# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos 
# e tenha fornecido um email válido. Escreva um programa que valide essas 
# condições e imprima "Dados de usuário válidos" ou o erro específico encontrado.

import re # regular expression

idade = 19
email = 'thiago@gmail.com.br'
email_valido = re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email)

print("email valido" if email_valido else "email invalido.")

if (idade >= 18 and idade <= 65) and email_valido:
    print("dados válidos")
else: print("dados inválidos")



