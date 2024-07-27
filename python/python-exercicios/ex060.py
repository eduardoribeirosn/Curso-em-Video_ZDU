n = int(input('Digite um número inteiro: '))
print('Calculando {}! =' .format(n), end=' ')
cont = n
fat = n
while cont != 1:
    print('{}' .format(cont), end=' ')
    if cont > 1:
        print('*', end=' ')
    if cont == 2:
        print('1', end=' ')
    fat =  fat * (cont - 1)
    cont -= 1
print('= {}' .format(fat))

# agora com for

# for c in range(n, 1, -1):
#     fat = fat * (c - 1)
# print('O fatorial de {} é {}!' .format(n, fat))