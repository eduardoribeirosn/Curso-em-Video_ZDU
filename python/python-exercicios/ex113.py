def leiaInt(text):
    while True:
        try:
            num = int(input(text))
        except (ValueError, TypeError):
            print(f'\033[1;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[1;33mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return num

def leiaReal(text):
    while True:
        try:
            num = float(input(text))
        except (ValueError, TypeError):
            print(f'\033[1;31mERRO! Digite um número Real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[1;33mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return num


inteiro = leiaInt('Digite um Inteiro: ')
real = leiaReal('Digite um Real: ')
print(f'\nO valor inteiro digitado foi {inteiro} e o real foi {real}!\n')
