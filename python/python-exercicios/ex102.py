def fatorial(num, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param num: O número a ser calculado.
    :param show: {opcional} Mostrar ou não a conta.
    :return: O valor do Fatorial de um número num.
    """
    print()
    print('-' * 40)
    f = 1
    for c in range(num, 0, -1):
        f *= c
    if show:
        conta = ''
        for c in range(num, 0, -1):
            conta += f'{c} '
            if c > 1:
                conta += f'* '
            elif c == 1:
                conta += f'= '
        conta += str(f)
        return conta
    else:
        return f


print(fatorial(int(input('Digite um número: ')), True))
# help(fatorial)
print()
