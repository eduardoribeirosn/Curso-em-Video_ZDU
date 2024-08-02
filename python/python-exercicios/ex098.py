from time import sleep
def contagem():
    print('-=' * 30)
    print(f'Contagem de 1 até 10 de 1 em 1')
    for cont in range(1, 10 + 1, 1):
        print(f'{cont}',  end=' ')
        # sleep(1)
    print('FIM!')
    print('-=' * 30)
    print(f'Contagem de 10 até 0 de 2 em 2')
    for cont in range(10, 0 -1, -2):
        print(f'{cont} ', end=' ')
        # sleep(1)
    print('FIM!')
    print('-=' * 30)
    print('Agora é sua vez de personalizar a contagem!')
    inicio = int(input(f'{"Início:":<8} '))
    fim = int(input(f'{"Fim:":<8} '))
    passo = int(input(f'{"Passo:":<8} '))
    print('-=' * 30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if passo == 0:
        passo += 1
    if fim < 0:
        if passo > 0:
            passo *= (-1)
    if fim < inicio and fim > 0 and passo >= 0:
        passo *= -1
    if fim >= 0 and fim > inicio:
        for cont in range(inicio, fim + 1, passo):
            print(f'{cont}', end=' ')
        print('FIM!')
    else:
        for cont in range(inicio, fim - 1, passo):
            print(f'{cont}', end=' ')
        print('FIM!')
contagem()