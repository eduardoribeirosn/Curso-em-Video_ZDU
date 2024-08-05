def ficha(jogador='<desconhecido>', gols=0):
    return f'O jogador {jogador} fez {gols} gol(s) no campeonato.'


print()
print('-' * 40)
nome = str(input('Nome do Jogador: '))
golsJ = str(input('Número de Gols: '))
if golsJ.isnumeric():
    int(golsJ)
else:
    golsJ = 0
if nome.strip() == '' and golsJ == '':
    print(ficha())
elif nome.strip() == '':
    print(ficha(gols=golsJ))
elif golsJ == '':
    print(ficha(jogador=nome))
else:
    print(ficha(nome, golsJ))

print()
