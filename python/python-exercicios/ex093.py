jogador = {}
golsp = []
totg = 0
nome = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {nome} jogou? R: '))
for c in range(0, partidas):
    gols = int(input(f'Quantos gols na partida {c + 1}? R: '))
    golsp.append(gols)
    totg += gols
jogador = {
    'Nome': nome,
    'Gols': golsp,
    'Total': totg
}
print('-=' * 30)
print(jogador)
print('-=' * 30)
print(f'O campo nome tem o valor {jogador["Nome"]}.')
print(f'O campo gols tem o valor {jogador["Gols"]}.')
print(f'O campo total tem o valor {jogador["Total"]}.')
print('-=' * 30)
print(f'O jogador Joelson jogou {partidas} partidas.')
for c in range(0, partidas):
    print(f'    => Na partida {c + 1}, fez {jogador["Gols"][c]} gols.')
print(f'Foi um total de {jogador["Total"]} gols.')
print()
