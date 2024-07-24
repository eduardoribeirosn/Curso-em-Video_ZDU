from random import randint
from time import sleep
n = int(randint(0, 10))
nt = 11
cont = 0
print('-=-' * 20)
print('Descubra em qual número eu pensei! 0 a 10')
print('-=-' * 20)
while n != nt:
    nt = int(input('\nQual número foi? R: '))
    cont += 1
    print('\nProcessando...\n')
    sleep(1)
    if (nt != n):
        print('Você errou!! Tente Novamente!')
print('\033[1:32mParabéns\033[m, Você Acertou!!')
if cont == 1:
    print('E precisou de {} chance' .format(cont))
else:
    print('E precisou de {} chances' .format(cont))
