import ex107

p = float(input('Digite o preço: R$'))
print(f'A metade de R${p} é R${ex107.metade(p)}')
print(f'O dobro de R${p} é R${ex107.dobro(p)}')
print(f'Aumentando 10%, temos R${ex107.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos R${ex107.diminuir(p, 13)}')