def areat(L, C):
    A = L * C
    print(f'A área de um terreno {L}x{C} é de {A}m².')


print('  Controle de Terrenos')
print('-' * 20)
L = float(input('LARGURA (m): '))
C = float(input('COMPRIMENTO (m): '))
areat(L, C)
