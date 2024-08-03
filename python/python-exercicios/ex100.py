from random import randint
from time import sleep
lista = []
print()
def sorteia():
    lista.clear()
    for c in range(1, 6):
        lista.append(randint(1, 10))
    print(f'Sorteando 5 valores da Lista: ', end='')
    for valor in lista:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.2)
    print(f'PRONTO!')

    
def somaPar():
    somaP = 0
    for valor in lista:
        if valor % 2 == 0:
            somaP += valor
    print(f'Somando os valores pares de {lista}, temos {somaP}')


sorteia()
somaPar()

print()
