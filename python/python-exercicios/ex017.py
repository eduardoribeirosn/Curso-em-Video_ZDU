from math import sqrt, pow
co = float(input('Digite o Cateto Oposto: '))
ca = float(input('Digite o Cateto Adjacente: '))
hi = sqrt((pow(co, 2) + pow(ca, 2)))
print('Com os Catetos sendo {} e {} a Hipotenusa é {:.2f}' .format(co, ca, hi))
