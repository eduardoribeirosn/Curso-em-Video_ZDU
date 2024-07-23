print('\033[0;34m{:=^40}\033[m'.format(' LOJAS ZDUARDO '))
preco = float(input('Preço do produto: R$'))
print('Ok..')
condicao = input('''Condição de pagamento?
[ Dinheiro ] à vista no Dinheiro (10% de Desconto)
[ Cheque ] Cheque (10% de Desconto)
[ Cartão ] Cartão (à vista = 5% de Desconto, 2x = 0% de Desconto, 3x = juros = 20%)
R: ''')
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
        print('Você pagará R${:.2f} SEM JUROS' .format(pagar))
        print('Cada parcela será R${:.2f}' .format(parcela))
    elif vezes >= 3:
        pagar = preco * 1.2
        parcela = pagar / vezes
        print('Pagando com cartão em {}x!' .format(vezes))
        print('Você pagará R${:.2f} COM JUROS' .format(pagar))
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
