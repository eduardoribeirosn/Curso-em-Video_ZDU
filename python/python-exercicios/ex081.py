lista = []
cont = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    cont += 1
    while True:
        option = str(input('Quer continuar? (S/N) R: ')).upper().strip()[0]
        if option == 'S' or option == 'N':
            break
    if option == 'N':
        print('-=' * 30)
        break
print(f'Você digitou {cont} elementos.')
print(f'Os valores em ordem descrescente são {sorted(lista, reverse=True)}')
if 5 in lista:
    print(f'O valor 5 faz parte da lista!')
else:
    print(f'O valor 5 não foi encontrado na lista')
