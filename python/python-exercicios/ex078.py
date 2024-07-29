lista = []
print('-=' * 30)
for cont in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {cont}: ')))
print('-=' * 30)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {max(lista)} nas posições', end=' ')
for maxi in range(0, len(lista)):
    if lista[maxi] == max(lista):
        print(lista.index(max(lista), maxi), end='... ')
print(f'\nO menor valor digitado foi {min(lista)} nas posições', end=' ')
for minu in range(0, len(lista)):
    if lista[minu] == min(lista):
        print(lista.index(min(lista), minu), end='... ')
