print('\033[1;33m-=-=-=-\033[0;37m Valor \033[1;33m-=-=-=-\033[m')
preco = float(input('Preço do produto: R$'))
print('Ok..')
condicao = input('Condição de pagamento? \n- Dinheiro;\n- Cheque;\n- Cartao.\nR: ')
if condicao.strip().lower() == 'cartao' or condicao.strip().lower() == 'cartão':
    vezes = int(input('Quantas vezes? (1 = a vista) R: '))
    if vezes == 1:
        pagar = preco * 0.95
        print('Pagando com cartão a vista!')
        print('Você pagará R${:.2f}' .format(pagar))
    elif vezes == 2:
        pagar = preco
        parcela = pagar / vezes
        print('Pagando com cartão em 2x!')
        print('Você pagará R${:.2f}' .format(pagar))
        print('Cada parcela será R${:.2f}' .format(parcela))
    elif vezes >= 3:
        pagar = preco * 1.2
        parcela = pagar / vezes
        print('Pagando com cartão em {}x!' .format(vezes))
        print('Você pagará R${:.2f}' .format(pagar))
        print('Cada parcela será R${:.2f}' .format(parcela))
elif condicao.strip().lower() == 'dinheiro':
    pagar = preco * 0.9
    print('Pagando com dinheiro!')
    print('Você pagará R${:.2f}' .format(pagar))
elif condicao.strip().lower() == 'cheque':
    pagar = preco * 0.9
    print('Pagando com cheque!')
    print('Você pagará R${:.2f}' .format(pagar))
else:
    print('Condição de Pagamento Inválida!')
