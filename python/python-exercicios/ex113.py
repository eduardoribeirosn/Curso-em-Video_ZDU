def leiaInt(text):
    num = input(text)
    while True:
        if num.isnumeric():
            int(num)
            break
        elif num == '':
            num = 0
            break
        else:
            print(f'\033[1;31mERRO! Digite um número inteiro válido.\033[m')
            num = input(text)
    return num

def leiaReal(text):
    num = input(text).strip().replace(',', '.')
    while True:
        if num.isalpha():
            print(f'\033[1;31mERRO! Digite um número Real válido.\033[m')
            num = input(text).strip().replace(',', '.')
        elif num == '':
            num = 0
            break
        else:
            float(num)
            break
    return num


inteiro = leiaInt('Digite um Inteiro: ')
real = leiaReal('Digite um Real: ')
print(f'\nO valor inteiro digitado foi {inteiro} e o real foi {real}!\n')
