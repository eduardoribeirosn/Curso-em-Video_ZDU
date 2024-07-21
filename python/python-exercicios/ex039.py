from datetime import date
print('\033[1;33m-=-=-=-\033[32mAlistamento\033[1;33m-=-=-=-\033[m')
anon = int(input('Em que ano você nasceu?: '))
anoa = date.today().year
idade = anoa - anon
if idade < 18:
    falta = 18 - idade
    print('Você ainda vai se alistar para o exército!')
    if falta == 1:
        print('Falta {} ano.' .format(falta))
    else:
        print('Faltam {} anos.' .format(falta))
elif idade == 18:
    print('Está na Hora de se Alistar!')
    print('Este é seu ano, Se aliste Já!!')
elif idade > 18:
    passou = idade - 18
    print('Já passou o tempo do alistamento!')
    if passou == 1:
        print('Já passou {} ano.' .format(passou))
    else:
        print('Já passou {} anos.' .format(passou))
