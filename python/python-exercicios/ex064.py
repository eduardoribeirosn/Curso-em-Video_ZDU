n = 0
soma = 0
cont = 0
while n != 999:
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
print('No total foram digitados {} vezes,\ne\nA soma de todos esses números foi: {}' .format(cont - 1, soma - 999))