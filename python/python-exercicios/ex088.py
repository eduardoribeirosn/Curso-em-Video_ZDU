from random import randint
mega = []
print('-' * 40)
print(f'{'JOGA NA MEGA SENA':^40}')
print('-' * 40)
jogos = int(input('Quantos jogos você quer que eu sorteie? R: '))
print(f'{f' SORTEANDO {jogos} JOGOS ':^35}')
for c in range(0, jogos):
    jogo = [randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60)]
    mega.append(jogo[:])
for j, jo in enumerate(mega):
    print(f'Jogo {j + 1}: {jo}')
print(f'{' < BOA SORTE! > ':^35}\n')
