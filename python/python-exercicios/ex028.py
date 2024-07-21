from random import randint
from time import sleep
n = int(randint(0, 5))

print('-=-' * 20)
print('Descubra em qual número eu pensei!')
print('-=-' * 20)
nt = int(input('Qual número foi? R: '))
print('Processando...')
sleep(3)
if (nt == n):
    print('Você acertou!!')
else:
    print('Você errou!!')
    print('O número foi {}' .format(n))
