maior = 0
masc = 0
fem20 = 0
while True:
    idade = int(input('Idade: '))
    if idade > 18:
        maior += 1
    sexo = 'A'
    while sexo != 'M' and sexo != 'F':
        sexo = input('Sexo (M/F): ').upper().strip()[0]
    if sexo == 'M':
        masc += 1
    if sexo == 'F':
        if idade < 20:
            fem20 += 1
    option = 'A'
    while option != 'S' and option != 'N':
        option = input('Deseja cadastra mais alguém? (S/N)\nR: ').upper().strip()[0]
    if option == 'S':
        print('\n')
    else:
        print('\nFinalizando...\n')
        break
if maior == 1:
    print(f'\nUma pessoa é maior que 18 anos!')
else:
    print(f'\n{maior} pessoas são maiores que 18 anos!')
if masc == 1:
    print(f'\nUm Homem foi cadastrado!')
else: 
    print(f'\n{masc} Homens foram cadastrados!')
if fem20 == 1:
    print(f'\nUma Mulher tem menos de 20 anos!\n')
else: 
    print(f'\n{fem20} Mulheres tem menos de 20 anos!\n')