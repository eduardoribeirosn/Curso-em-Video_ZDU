banco = 'BANCO CEV'
print('=' * 35)
print(f'{banco:^35}')
print('=' * 35)
# valor = int(input('Que valor você quer sacar? R$'))
# nota50 = valor // 50
# nota20 = (valor % 50) // 20
# nota10 = ((valor % 50) % 20) // 10
# nota1 = (((valor % 50) % 20) % 10) // 1
# print(f'Total de {nota50} cédulas de R$50')
# print(f'Total de {nota20} cédulas de R$20')
# print(f'Total de {nota10} cédulas de R$10')
# print(f'Total de {nota1} cédulas de R$1')
# print('=' * 35)
# print('Volte sempre ao BANCO CEV! Tenha um bom dia!\n')



# Resolução do Prof Guanabara

valor = int(input('Que valor você quer sacar? R$'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')