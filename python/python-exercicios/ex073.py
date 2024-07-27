tabela = ('Santos', 'Vila Nova', 'América MG', 'Grêmio Novorizontino SP', 'Mirassol', 'Operário Ferroviário', 'Goiás', 'Ceará', 'Recife', 'Avaí', 'CR Brasil', 'Ponte Preta', 'Payssandu', 'Amazonas', 'Coritiba', 'Chapecoense', 'Botafogo SP', 'Brusque', 'Ituano SP', 'Guarani SP')

print('-' * 40)
for pos, time in enumerate(tabela, 0):
    if pos == 5:
        break
    print(f'{pos + 1}° - {time}')
# print(tabela[0:5])
# print('')
print('=' * 40)
print('-' * 40)
for pos, time in enumerate(tabela, 0):
    if pos >= (20-4):
        print(f'{pos + 1}° - {time}')
# print(tabela[-4:])
print('=' * 40)
print('~' * 40)
for cont in sorted(tabela):
    print(f'{cont} -', end=' ')
#print(sorted(tabela))
print('')
print('~' * 40)
# print('')
print('-=' * 20)
print(f'O time Chapecoense está na Posição: {tabela.index('Chapecoense')}')
print('-=' * 20)
