cond = 0
while cond != 5:
    v1 = float(input('\nDigite o primeiro valor: '))
    v2 = float(input('Digite o segundo valor: '))
    print('''
    \033[31m[1]\033[35m Somar
    \033[31m[2]\033[35m Multiplicar
    \033[31m[3]\033[35m Maior
    \033[31m[4]\033[35m Novos números
    \033[31m[5]\033[35m Sair do programa\033[m
    ''')
    cond = int(input('Digite uma opção: '))
    if cond == 1:
        soma = v1 + v2
        print('A soma dos números é = {}' .format(soma))
    elif cond == 2: 
        mult = v1 * v2
        print('A multiplicação dos números é = {}' .format(mult))
    elif cond == 3:
        if v1 > v2:
            print('\nO primeiro valor ({}) é o MAIOR\ne\nO segundo valor ({}) é o MENOR' .format(v1, v2))
        elif v1 < v2:
            print('\nO segundo valor ({}) é o MAIOR\ne\nO primeiro valor ({}) é o MENOR' .format(v2, v1))
        else:
            print('\nOs valores {} e {} são iguais!' .format(v1, v2))
    elif cond == 4:
        print('\nDigite os números novamente!')
    elif cond == 5:
        print('\nFinalizando...')
    elif cond != 1 and cond != 2 and cond != 3 and cond != 4 and cond != 5:
        print('Digite os números novamente, e coloque uma opção valida (1 a 5)')