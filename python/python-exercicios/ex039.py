from datetime import date
print('\033[1;33m-=-=-=-\033[32mAlistamento\033[1;33m-=-=-=-\033[m')
sexo = int(input('Você é (1 - Homem ou 2 - Mulher)? \nR: '))
if sexo == 1:
    anon = int(input('Em que ano você nasceu? \nR: '))
    anoa = date.today().year
    idade = anoa - anon
    if idade < 18:
        falta = 18 - idade
        print('Você ainda vai se alistar para o exército! no ano {}' .format(anoa + falta))
        if falta == 1:
            print('Falta {} ano.' .format(falta))
        else:
            print('Faltam {} anos.' .format(falta))
    elif idade == 18:
        print('Está na Hora de se Alistar! ano {}' .format(anoa))
        print('Este é seu ano, Se aliste Já!!')
    elif idade > 18:
        passou = idade - 18
        print('Já passou o tempo do alistamento! você se alistou no ano {}' .format(anoa - passou))
        if passou == 1:
            print('Já passou {} ano.' .format(passou))
        else:
            print('Já passou {} anos.' .format(passou))
else:
    print('Você não precisa se alistar!')
