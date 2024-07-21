velo = float(input('Qual a velocidade do carro? R: '))
if (velo > 80.0):
    multa = (velo - 80) * 7
    print('Você foi mutado! você excedeu o limite de 80Km/h')
    print('E sua multa irá custar: {:.2f}' .format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança!')
