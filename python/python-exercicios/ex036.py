print('-=-=-=-\033[1;31mBanco\033[m-=-=-=-')
vcasa = float(input('Qual o Valor da Casa? R: R$'))
print('Ok...')
sal = float(input('Qual o seu Salário? R: R$'))
print('Ok...')
temp = float(input('Em quantos anos pretende pagar? R: '))
meses = temp * 12
vprest = vcasa / meses
if (sal * 0.3) < vprest:
    print('\033[1;35mEmpréstimo\033[31m Negado\033[0;37!!\033[m')
else:
    print('\033[1;35mEmpréstimo\033[32m Aceito\033[0;37!!\033[m')
