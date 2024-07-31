from random import randint
from time import sleep
mega = []
print('-' * 40)
print(f'{'JOGA NA MEGA SENA':^40}')
print('-' * 40)
jogos = int(input('Quantos jogos você quer que eu sorteie? R: '))
print(f'{f' SORTEANDO {jogos} JOGOS ':^35}')
for c in range(0, jogos):
    jogo = []
    for cc in range(0, 6):
        while True:
            jogo1 = randint(0, 60)
            if jogo1 not in jogo:
                jogo.insert(cc, jogo1)
                break
    mega.append(jogo[:])
    mega[c].sort()
    jogo.clear()
for j, jo in enumerate(mega):
    sleep(1)
    print(f'Jogo {j + 1}: {jo}')
print(f'{' < BOA SORTE! > ':^35}\n')
