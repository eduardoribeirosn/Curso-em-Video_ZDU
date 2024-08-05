def leiaInt(text):
    num = input(text)
    while True:
        if num.isnumeric():
            int(num)
            break
        else:
            print(f'\033[1;31mERRO! Digite um número inteiro válido.\033[m')
            num = input(text)
    return f'Você acabou de digitar o número {num}'


print('\n', leiaInt('Digite um número: '), '\n')
