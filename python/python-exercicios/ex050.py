s = 0
cont = 0
for c in range(1, 7, 1):
    n = int(input('Digite o {}° valor: ' .format(c)))
    if (n % 2) == 0:
        s += n
        cont += 1
if cont == 1:
    print('Você informou {} número par e a soma dele foi {}' .format(cont, s))
else:
    print('Você informou {} números pares e a soma deles foi {}' .format(cont, s))