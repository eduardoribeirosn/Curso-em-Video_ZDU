while True:
    num = int(input('\nTabuada = Número: '))
    for c in range(1, 11, 1):
        print('{} * {} = {}' .format(num, c, num * c))
    if num < 0:
        break
print('\nPROGRAMA TABUADA ENCERRADO. Volte sempre!')