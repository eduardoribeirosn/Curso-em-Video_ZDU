from random import randint
contV = 0
print('=-' * 15)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-' * 15)
while True:
    # 1 = Par --- 2 = Impar
    # pcPI = randint(1, 2)
    pcNum = randint(0, 9)
    vcPI = 'A'
    while vcPI != 'P' and vcPI != 'I':
        vcPI = input('\nPar ou Impar? (P/I) R: ').strip().upper()[0]
        if vcPI != 'P' and vcPI != 'I':
            print('Existe apenas a Opção (P) e a (I)')
    vcNum = int(input('Escolha um número: '))
    print('-' * 20)
    print(f'Você jogou {vcNum} e o computador {pcNum}. Total de {vcNum + pcNum} DEU', end=' ')
    par = ((vcNum + pcNum) % 2) == 0
    if par == True:
        print('PAR')
        print('-' * 25)
    else:
        print('IMPAR')
        print('-' * 25)
    if vcPI == 'P':
        if par == True:
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            print('=-' * 10)
            contV += 1
        else:
            print('Você PERDEU!')
            print('=-' * 10)
            break
    if vcPI == 'I':
        impar = ((vcNum + pcNum) % 2) != 0
        if impar == True:
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            print('=-' * 10)
            contV += 1
        else:
            print('Você PERDEU!')
            print('=-' * 10)
            break
if contV == 1:
    print(f'GAME OVER! Você Venceu {contV} vez!')
else:
    print(f'GAME OVER! Você Venceu {contV} vezes!')


