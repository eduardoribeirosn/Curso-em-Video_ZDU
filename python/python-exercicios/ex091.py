from random import randint
from time import sleep
jogadores = []
jogador1 = {'Nome': 'jogador1'}
jogador2 = {'Nome': 'jogador2'}
jogador3 = {'Nome': 'jogador3'}
jogador4 = {'Nome': 'jogador4'}
jogadores.append(jogador1)
jogadores.append(jogador2)
jogadores.append(jogador3)
jogadores.append(jogador4)
for c in range(0, 4):
    dado = randint(1, 6)
    jogadores[c]['dado'] = f'{dado}'
print('Valores sorteados:')
for n, player in enumerate(jogadores):
    print(f'    O {player['Nome']} tirou {player['dado']}')
print('Ranking dos jogadores:')
jogadores = sorted(jogadores, key=lambda x: x['dado'], reverse=True)
for pos, player in enumerate(jogadores):
    print(f'    {pos +1}° lugar: {player['Nome']} com {player['dado']}')
