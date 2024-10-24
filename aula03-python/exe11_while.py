# Exemplo Prático: while True com Pausa
# Um exemplo direto do uso de while True em Python é criar 
# um loop infinito que executa uma ação a cada intervalo definido, 
# como imprimir uma mensagem a cada 10 segundos. 
# Isso pode ser útil para monitorar processos ou dados em tempo real com uma verificação periódica.

import time

while True:
    print('verificando novos dados...')
    # Aqui você pode adicionar o código para verificar novos dados,
    # por exemplo, checar a existência de novos arquivos em um diretório,
    # fazer uma consulta a um banco de dados ou API, etc.
    
    time.sleep(10)  # Pausa o loop por 10 segundos