from random import randint
from time import sleep
print('\033[1;33m-=-=-=-\033[0;34m Jokenpô \033[1;33m-=-=-=-\033[m')
escolhas = ['Pedra', 'Papel', 'Tesoura']
# Pode ser esse jeito ou pc = random.choice(escolhas)
pc = randint(0, 2)
print(escolhas[0])
print('Escolha um: \n1 - Pedra\n2 - Papel\n3 - Tesoura')
vc = int(input('R: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-=' * 11)
print('Computador jogou {}' .format(escolhas[pc]))
print('Jogador jogou {}' .format(escolhas[vc - 1]))
print('-=' * 11)
if vc == 1:
    if escolhas[pc] == escolhas[0]:
        print('Empate')
    elif escolhas[pc] == escolhas[1]:
        print('Computador Vence')
    elif escolhas[pc] == escolhas[2]:
        print('Jogador Venceu')
elif vc == 2:
    if escolhas[pc] == escolhas[0]:
        print('Jogador Venceu')
    elif escolhas[pc] == escolhas[1]:
        print('Empate')
    elif escolhas[pc] == escolhas[2]:
        print('Computador Vence')
elif vc == 3:
    if escolhas[pc] == escolhas[0]:
        print('Computador Vence')
    elif escolhas[pc] == escolhas[1]:
        print('Jogador Venceu')
    elif escolhas[pc] == escolhas[2]:
        print('Empate')