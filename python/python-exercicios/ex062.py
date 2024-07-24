p1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite o número da razão: '))
cont = 1
option = 0
while cont != 11:
    print('{} ->' .format(((cont - 1) * r) + p1), end=' ')
    cont += 1
while option != 2:
    while option != 1 and option != 2:
        option = int(input('\nDeseja continuar a PA? (1 - Sim / 2 - Não)\nR: '))
    if option == 1:
        ultimo = cont
        final = int(input('\nMais quantos números? R: '))
        while cont != (final + ultimo):
            print('{} ->' .format(((cont - 1) * r) + p1), end=' ')
            cont += 1
        option = 0
    elif option == 2:
        print('\nFinalizando...\n')
