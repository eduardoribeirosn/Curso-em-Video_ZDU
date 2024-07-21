sal = float(input('Digite um salário: R$'))
if (sal > 1250):
    nsal = sal * 1.1
    print('Seu salário era R${:.2f}, agora é R${:.2f}' .format(sal, nsal))
else:
    nsal = sal * 1.15
    print('Seu salário era R${:.2f}, agora é R${:.2f}' .format(sal, nsal))