numbers = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if 0 <= n <= 20:
            break
        print('Tente Novamente!', end=' ')
    print(f'Você digitou o número {numbers[n]}')
    while True:
        option = str(input('Você quer continuar? (S/N) R: ')).upper().strip()[0]
        if option == 'S' or option == 'N':
            break
    if option == 'N':
        break
print('\nFinalizando...\n')