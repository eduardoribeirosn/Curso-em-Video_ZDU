# Método Zdu
# from time import sleep
# peso = []
# for c in range(0, 5, 1):
#     peso.append(float(input('Digite um peso: ')))
# peso.sort()
# print('\nCalculando...\n')
# sleep(2)
# print('O maior peso foi: {}\ne\nO menor peso foi: {}' .format( peso[len(peso) - 1], peso[0]))


# Método prof

maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}° pessoa: ' .format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi {}Kg' .format(maior))
print('O menor peso lido foi {}Kg' .format(menor))
