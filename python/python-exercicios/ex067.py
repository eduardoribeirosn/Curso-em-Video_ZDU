while True:
    num = int(input('\nTabuada = Número: '))
    if num < 0:
        break
    print('-' * 30)
    for c in range(1, 11, 1):
        print('{} * {} = {}' .format(num, c, num * c))
    print('-' * 30)
print('\nPROGRAMA TABUADA ENCERRADO. Volte sempre!')