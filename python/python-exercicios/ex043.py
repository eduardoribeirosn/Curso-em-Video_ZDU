print('\033[1;33m-=-=-=-\033[0;36m I M C \033[1;33m-=-=-=-\033[m')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura em metros: '))
altura *= 100
imc = peso / altura ** 2
imc = imc * 10000
print('IMC = {:.1f}' .format(imc))
if imc < 18.5:
    print('Abaixo do Peso!')
elif imc >= 18.5 and imc < 25:
    print('Peso Ideal!')
elif imc >= 25 and imc < 30:
    print('Sobrepeso!')
elif imc >= 30 and imc <= 40:
    print('Obesidade!')
elif imc > 40:
    print('Obesidade mórbida!')
    