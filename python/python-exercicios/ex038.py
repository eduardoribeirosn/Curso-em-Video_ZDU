print('\033[1;33m-=-=-=-\033[32mMaior\033[0;30m ou \033[1;31mMenor\033[1;33m-=-=-=-\033[m')
n1 = int(input('Digite o Primeiro número: '))
n2 = int(input('Digite o Segundo número: '))

if n1 > n2:
    print('\nO primeiro valor ({}) é maior' .format(n1))
elif n2 > n1:
    print('\nO segundo valor ({}) é maior' .format(n2))
elif n1 == n2:
    print('\nNão existe valor maior, os dois são iguais ({} = {})' .format(n1, n2))