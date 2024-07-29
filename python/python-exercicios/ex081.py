lista = []
cont = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    while True:
        option = str(input('Quer continuar? (S/N) R: ')).upper().strip()[0]
        if option == 'S' or option == 'N':
            break
    if option == 'N':
        print('-=' * 30)
        break
print(f'Você digitou {len(lista)} elementos.')
# CASO QUEIRA USAR O lista.sort(reverse=True), use ele fora do print, e depois dentro do print coloque apenas a LISTA.
print(f'Os valores em ordem descrescente são {sorted(lista, reverse=True)}')
if 5 in lista:
    print(f'O valor 5 faz parte da lista!')
else:
    print(f'O valor 5 não foi encontrado na lista')
