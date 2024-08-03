from datetime import date
anoA = date.today().year
def votos(voto):
    idade = anoA - voto
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    elif idade >= 18 and idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
print()
print('-' * 40)
anoN = int(input('Em que ano você nasceu? R: '))
print(votos(anoN))
print()
