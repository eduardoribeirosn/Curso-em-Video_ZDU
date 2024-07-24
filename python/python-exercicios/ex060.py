n = int(input('Digite um número inteiro: '))
# cont = n
fat = n
# while cont != 1:
#     fat =  fat * (cont - 1)
#     cont -= 1
# print('O fatorial de {} é {}!' .format(n, fat))

# agora com for

for c in range(n, 1, -1):
    fat = fat * (c - 1)
print('O fatorial de {} é {}!' .format(n, fat))