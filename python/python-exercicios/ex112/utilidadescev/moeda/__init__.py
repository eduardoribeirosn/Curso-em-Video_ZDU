def metade(num, formato=False):
    r = num / 2
    if formato:
        return moeda(r)
    else:
        return r


def dobro(num, formato=False):
    r = num * 2
    if formato:
        return moeda(r)
    else:
        return r


def aumentar(num, x, formato=False):
    r = num * (1 + (x / 100))
    if formato:
        return moeda(r)
    else:
        return r


def diminuir(num, x, formato=False):
    r = num * (1 - (x / 100))
    if formato:
        return moeda(r)
    else:
        return r


def moeda(num):
    num = f'R${num:.2f}'
    return num


def resumo(num, a, r):
    p = moeda(num)
    dobrar = dobro(num, True)
    metades = metade(num, True)
    aumento = aumentar(num, a, True)
    reducao = diminuir(num, r, True)
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'{"Preço analisado:":<20}{p}')
    print(f'{"Dobro do preço:":<20}{dobrar}')
    print(f'{"Metade do preço:":<20}{metades}')
    print(f'{f"{a}% de aumento:":<20}{aumento}')
    print(f'{f"{r}% de redução:":<20}{reducao}')
    print('-' * 30)


