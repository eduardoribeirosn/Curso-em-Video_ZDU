import random
print('\033[1;33m-=-=-=-\033[0;34m Jokenpô \033[1;33m-=-=-=-\033[m')
escolhas = ['Pedra', 'Papel', 'Tesoura']
pc = random.choice(escolhas)
print('Escolha um: \n1 - Pedra\n2 - Papel\n3 - Tesoura')
vc = int(input('R: '))
if vc == 1:
    if pc == 'Pedra':
        print('Empate')
    elif pc == 'Papel':
        print('Perdeu')
    elif pc == 'Tesoura':
        print('Ganhou')
elif vc == 2:
    if pc == 'Pedra':
        print('Ganhou')
    elif pc == 'Papel':
        print('Empate')
    elif pc == 'Tesoura':
        print('Perdeu')
elif vc == 3:
    if pc == 'Pedra':
        print('Perdeu')
    elif pc == 'Papel':
        print('Ganhou')
    elif pc == 'Tesoura':
        print('Empate')