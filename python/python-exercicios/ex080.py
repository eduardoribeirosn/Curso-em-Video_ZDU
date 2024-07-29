lista = []
for cont in range(1, 6):
    n = int(input('Digite um valor: '))
    if len(lista) == 0 or n > max(lista):
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        for c in range(0, 4):
            if n < lista[c]:
                lista.insert(c, n)
                print(f'Adicionado na posição {c} da lista...')
                break
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}\n')

