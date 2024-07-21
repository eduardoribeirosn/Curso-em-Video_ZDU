print('\033[1;33m-=-=-=-\033[36m Notas \033[1;33m-=-=-=-\033[m')
n1 = float(input('Digite sua primeira nota: '))
print('Ok..')
n2 = float(input('Digite sua segunda nota: '))
print('Ok..')
media = (n1 + n2) / 2
if media < 5:
    print('\033[1;31mReprovado\033[m!!')
elif media >= 5 and media < 7:
    print('\033[1;35mRecuperação\033[m!!')
elif media >= 7:
    print('\033[1;32mAprovado\033[m!!')