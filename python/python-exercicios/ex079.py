lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print(f'Valor duplicado! Não vou adicionar...')
    while True:
        option = input('Quer continuar? (S/N) R: ').upper().strip()[0]
        if option == 'S' or  option == 'N':
            break
    if option == 'N':
        break
print('-=' * 30)
print(f'Você digitou os valores {sorted(lista)}')
