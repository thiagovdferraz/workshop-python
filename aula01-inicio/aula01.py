print('Olá!')

print("segunda alteração...")

# git config --global user.name "Seu Nome"
# git config --global user.email "seu.email@exemplo.com"
# git config --global --list

# git init
# git status
# git add file
# git commit -m "mensagem"
# git log
# git restore file - volta para o último commit feito

print("terceira alteração...")
print("quarta modificação...")
print("quinta modificação...")

#git commit --amend: reescreve a ultima mensagem do ultimo commit

# git checkout hash_num: volta paraq o estado daquele momento

# o que é branch
# Branches são como linhas do tempo paralelas no seu repositório.
# Elas permitem que você trabalhe em diferentes funcionalidades ou correções de bugs sem afetar a main.

# git merge
# apos realizar alterações em outro branch - task1, como podemos jogar em produção?
# usamos o git merge ticket-1

# passos
# git checkout main
# git merge task-1

# deletar ticket-1, pois nao precisamos mais dele
# git branch -d ticket-1