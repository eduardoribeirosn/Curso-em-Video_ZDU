# from random import randint
# from time import sleep
# jogadores = []
# jogador1 = {'Nome': 'jogador1'}
# jogador2 = {'Nome': 'jogador2'}
# jogador3 = {'Nome': 'jogador3'}
# jogador4 = {'Nome': 'jogador4'}
# jogadores.append(jogador1)
# jogadores.append(jogador2)
# jogadores.append(jogador3)
# jogadores.append(jogador4)
# for c in range(0, 4):
#     dado = randint(1, 6)
#     jogadores[c]['dado'] = f'{dado}'
# print('Valores sorteados:')
# for n, player in enumerate(jogadores):
#     print(f'    O {player['Nome']} tirou {player['dado']}')
# print('Ranking dos jogadores:')
# jogadores = sorted(jogadores, key=lambda x: x['dado'], reverse=True)
# for pos, player in enumerate(jogadores):
#     print(f'    {pos +1}° lugar: {player['Nome']} com {player['dado']}')

# OUUUUUUUUUUUUUUUUU

from random import randint
from time import sleep
from operator import itemgetter
jogo = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('  == RANKING DOS JOGADORES == ')
for i, v in enumerate(ranking):
    print(f'    {i + 1}° lugar: {v[0]} com {v[1]}')
    sleep(1)
