matriz = [[], [], []]
pares = somat = maior = 0
for c in range(0, 3):
    matriz[0].append(int(input(f'Digite um valor para [0, {c}]: ')))
for c in range(0, 3):
    matriz[1].append(int(input(f'Digite um valor para [1, {c}]: ')))
for c in range(0, 3):
    matriz[2].append(int(input(f'Digite um valor para [2, {c}]: ')))
print('-=' * 30)
for pos, n in enumerate(matriz[0]):
    print(f'[ {n} ]', end=' ')
print()
for pos, n in enumerate(matriz[1]):
    print(f'[ {n} ]', end=' ')
print()
for pos, n in enumerate(matriz[2]):
    print(f'[ {n} ]', end=' ')
print()
for c, n in enumerate(matriz):
    for cc, nn in enumerate(matriz[0]):
        if matriz[c][cc] % 2 == 0:
            pares += matriz[c][cc]
for c in range(0, 3):
    somat += matriz[c][2]
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    else:
        if matriz[1][c] > maior:
            maior = matriz[1][c]
print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {somat}')
print(f'O maior valor da segunda linha é {maior}')
