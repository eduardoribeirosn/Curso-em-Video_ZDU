loja = 'LOJA SUPER BARATÃO'
print('-' * 40)
print(f'{loja:^40}')
print('-' * 40)
cont = total = maior = barato = 0
nomeBarato = ''
while True:
    option = 'A'
    nProduto = input('Nome do Produto: ')
    preco = int(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        maior += 1
    if cont == 1:
        barato = preco
        nomeBarato = nProduto
    else:
        if barato > preco:
            barato = preco
            nomeBarato = nProduto
    while option != 'S' and option != 'N':
        option = input('Quer continuar? (S/N) R: ').upper().strip()[0]
    if option == 'N':
        print('\nFinalizando...\n')
        break
    
print(f'O total da compra foi R${total}')
print(f'Temos {maior} produtos custando mais de R$1000')
print(f'O produto mais barato foi "{nomeBarato}" que custa R${barato}')