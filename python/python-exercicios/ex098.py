from time import sleep
def contagem(I, F, P):
    if P == 0:
        P += 1
    print('-=' * 30)
    print(f'Contagem de {I} até {F} de {P} em {P}')
    if F < I:
        if I > F:
            if P > 0:
                P *= (-1)
    # if F < I and F >= 0 and P >= 0:
    #     P *= -1
    # if F >= 0 and F > I or F > I:
    #     for cont in range(I, F + 1, P):
    #         print(f'{cont}', end=' ')
    #     print('FIM!')
    # else:
    #     for cont in range(I, F - 1, P):
    #         print(f'{cont}', end=' ')
    #     print('FIM!')
    cont = I
    sleep(2.5)
    if I > F:
        while cont >= F:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont += P
    elif I < F:
        while cont <= F:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont += P
    print('FIM!')
    print('-=' * 30)



contagem(1, 10, 1)
contagem(10, 0, 2)
contagem(int(input('Digite o começo: ')), int(input('Digite o Fim: ')), int(input('Digite o passo: ')))
# contagem(5, -5, 0)
# contagem(10, 20, 1)
# contagem(20, 10, 1)
