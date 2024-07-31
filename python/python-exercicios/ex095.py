jogadores = []
jogador = {}
totg = 0
while True:
    golsp = []
    print('-' * 50)
    nome = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {nome} jogou? R: '))
    for c in range(0, partidas):
        gols = int(input(f'Quantos gols na partida {c + 1}? R: '))
        golsp.append(gols)
        totg += gols
    jogador = {
        'Nome': nome,
        'Gols': golsp[:],
        'Total': totg
    }
    jogadores.append(jogador.copy())
    del jogador
    golsp.clear()
    while True:
        option = str(input('Quer continuar? (S/N) R: ')).strip().upper()[0]
        if option == 'S' or option == 'N':
            break
    if option == 'N':
        print('-=' * 30)
        break
print(jogadores)
print(f'{"Cod":<4}{"Nome":<15}{"Gols":<15}{"Total":<6}')
print('-' * 40)
for c in range(0, len(jogadores)):
    print(f'{c:>3} {jogadores[c]["Nome"]:<15}{jogadores[c]["Gols"]}     {jogadores[c]["Total"]:<6}')
print('-' * 40)
while True:
    dados = int(input('Mostrar dados de qual jogador? (999 para interromper) R: '))
    if dados == 999:
        break
    elif dados < 0 or dados > len(jogadores) - 1:
        print(f'ERRO! não existe jogador com código {dados}! Tente Novamente')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[dados]['Nome']}')
        for cont in range(0, len(jogadores[dados]["Gols"])):
            print(f'No jogo {cont + 1} fez {jogadores[dados]["Gols"][cont]} gols.')
        print('-' * 40)





# print('-=' * 30)
# print(jogador)
# print('-=' * 30)
# print(f'O campo nome tem o valor {jogador["Nome"]}.')
# print(f'O campo gols tem o valor {jogador["Gols"]}.')
# print(f'O campo total tem o valor {jogador["Total"]}.')
# print('-=' * 30)
# print(f'O jogador Joelson jogou {partidas} partidas.')
# for c in range(0, partidas):
#     print(f'    => Na partida {c + 1}, fez {jogador["Gols"][c]} gols.')
# print(f'Foi um total de {jogador["Total"]} gols.')
# print()
