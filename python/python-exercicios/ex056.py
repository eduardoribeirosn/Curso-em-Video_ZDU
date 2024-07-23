from time import sleep
totalI = 0
cont = 0
maisVelho = ''
maisVelhoI = 0
mulherNova = 0
for c in range(0, 4, 1):
    print('----- {}° PESSOA -----' .format(c + 1))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo: (M/F) ')
    totalI += idade
    cont += 1
    if sexo.lower() == 'm':
        if idade > maisVelhoI:
            maisVelhoI = idade
            maisVelho = nome
    if sexo.lower() == 'f':
        if idade < 20:
            mulherNova += 1
mediaI = totalI / cont
print('\nCalculando...\n')
sleep(2)
print('A média de Idade do grupo é: {}' .format(mediaI))
print('O nome do Homem mais velho é: {}' .format(maisVelho))
if mulherNova == 1:
    print('{} mulher tem menos de 20 anos' .format(mulherNova))
else:
    print('{} mulheres tem menos de 20 anos' .format(mulherNova))

