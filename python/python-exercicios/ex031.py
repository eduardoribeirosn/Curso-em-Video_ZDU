dt = float(input('Qual a distância em Km da viagem: '))
if (dt <= 200):
    preco = dt * 0.5
    print('A viagem custará R${}' .format(preco))
else:
    preco = dt * 0.45
    print('A viagem custará R${}' .format(preco))
    