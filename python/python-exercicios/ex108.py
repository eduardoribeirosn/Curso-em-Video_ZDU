import ex107

p = float(input('Digite o preço: R$'))
print(f'A metade de {ex107.moeda(p)} é {ex107.moeda(ex107.metade(p))}')
print(f'O dobro de {ex107.moeda(p)} é {ex107.moeda(ex107.dobro(p))}')
print(f'Aumentando 10%, temos {ex107.moeda(ex107.aumentar(p, 10))}')
print(f'Reduzindo 13%, temos {ex107.moeda(ex107.diminuir(p, 13))}')