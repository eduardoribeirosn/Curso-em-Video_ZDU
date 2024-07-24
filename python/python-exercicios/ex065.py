cont = 0
option = 0
maior = 0
menor = 0
soma = 0
while option != 2:
    option = 0
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = n
        menor = n
    elif cont > 1:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    while option != 1 and option != 2:
        option = int(input('Deseja digitar mais valores? (1 - Sim / 2 - Não)\nR: '))
media = soma / cont
print('\nA média foi: {}' .format(media))
print('\nO maior foi: {}' .format(maior))
print('\nO menor foi: {}' .format(menor))
