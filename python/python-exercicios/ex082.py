listaC = []
listaP = []
listaI = []
while True:
    n = int(input('Digite um número: '))
    listaC.append(n)
    while True:
        option = str(input('Quer continuar? (S/N) R: ')).upper().strip()[0]
        if option == 'S' or option == 'N':
            break
    if option == 'N':
        break
for cont1 in listaC:
    if cont1 % 2 == 0:
        listaP.append(cont1)
for cont2 in listaC:
    if cont2 % 2 == 1:
        listaI.append(cont2)
print(f'A lista completa é {listaC}')
print(f'A lista de pares é {listaP}')
print(f'A lista de ímpares é {listaI}')
