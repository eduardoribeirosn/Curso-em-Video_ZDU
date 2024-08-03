def ficha(jogador='<desconhecido>', gols=0):
    return f'O jogador {jogador} fez {gols} gol(s) no campeonato.'


print()
print('-' * 40)
nome = str(input('Nome do Jogador: '))
golsJ = input('Número de Gols: ')
if nome == '' and golsJ == '':
    print(ficha())
elif nome == '':
    print(ficha(gols=golsJ))
elif golsJ == '':
    print(ficha(jogador=nome))
else:
    print(ficha(nome, golsJ))

print()
