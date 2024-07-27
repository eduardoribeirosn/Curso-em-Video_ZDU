n = int(input('Digite um número inteiro: '))
cont = 1
fibo = 0
save = 0
# print('0', end=' ')
while cont <= n:
    print('-> {}' .format(fibo), end=' ')
    fibo = fibo + save
    save = fibo - save
    if fibo == 0:
        fibo += 1
    cont += 1