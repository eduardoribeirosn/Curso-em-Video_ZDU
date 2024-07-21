print('\033[1;33m-=-=-=-\033[35m Categoria Natação \033[1;33m-=-=-=-\033[m')
idade = int(input('Digite sua Idade: '))
cores = {
    'nd': '\033[m',
    'classe': '\033[1;34m',
}
if idade <= 9:
    print('Sua categoria é {}Mirim{}' .format(cores['classe'], cores['nd']))
elif idade <= 14:
    print('Sua categoria é {}Infantil{}' .format(cores['classe'], cores['nd']))
elif idade <=19:
    print('Sua categoria é {}Junior{}' .format(cores['classe'], cores['nd']))
elif idade <=20:
    print('Sua categoria é {}Sênior{}' .format(cores['classe'], cores['nd']))
else:
    print('Sua categoria é {}Master{}' .format(cores['classe'], cores['nd']))