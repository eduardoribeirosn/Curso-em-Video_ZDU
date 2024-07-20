kmp = float(input('Digite a quantidade de Km percorrido pelo carro: '))
diaa = int(input('Digite a quantidade de dias que o carro foi alugado: '))
preco = (diaa * 60) + (kmp * 0.15)
print('O preço a pagar é: R${:.2f}' .format(preco))