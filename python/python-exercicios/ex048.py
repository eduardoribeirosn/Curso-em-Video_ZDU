s = 0
cont = 0
for c in range(3, 500, 3):
    if (c % 2) == 1:
        if (c % 3) == 0:
            s += c
            cont += 1
print('A soma de todos os {} valores solicitados é {}' .format(cont, s))
