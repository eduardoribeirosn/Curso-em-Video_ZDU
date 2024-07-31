galera = []
pessoa = []
mai = men = 0
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    galera.append(pessoa[:])
    if len(galera) == 1:
        mai = men = pessoa[1]
    else:
        if pessoa[1] > mai:
            mai = pessoa[1]
        elif pessoa[1] < men:
            men = pessoa[1]
    pessoa.clear()
    while True:
        option = str(input('Quer continuar? (S/N) R: ')).strip().upper()[0]
        if option == 'S' or option == 'N':
            break
        else:
            print('Use (S) ou (N)', end=' ')
    if option == 'N':
        break
print('-=' * 30)
print(f'Ao todo você cadastrou {len(galera)} pessoas.')
print(f'O maior peso foi de {mai}Kg. Peso de ', end=' ')
for c, p in enumerate(galera): # ou for p in galera:
    if galera[c][1] == mai: # ou if p[1] == mai:
        print(f'[{galera[c][0]}]', end=' ') # p[0]
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end=' ')
for c, p in enumerate(galera):
    if galera[c][1] == men:
        print(f'[{galera[c][0]}]', end=' ')
