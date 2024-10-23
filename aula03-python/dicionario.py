texto = 'hoje e nossa segunda aula do bootcamp , bootcamp de python'

novo_texto = texto.replace(",", "")
palavras = novo_texto.split(" ")
print(palavras)

# dicionario
contagem_palavras = {}

# quero percorrer todas as palavras dentro de palavras e checar
# se ela esta no meu contagem de palavras

for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra]=+1
    else:
        contagem_palavras[palavra]=1
