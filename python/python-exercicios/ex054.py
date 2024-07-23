from datetime import date
anoa = date.today().year
totalMaior = 0
totalMenor = 0
for c in range(0, 7, 1):
    ano = int(input('Digite o ano de Nascimento: '))
    if (anoa - ano) >= 21:
        totalMaior += 1
    else:
        totalMenor += 1
print('{} Não atingiram a Maior Idade!\ne\n{} Já atingiram a Maior Idade!' .format(totalMenor, totalMaior))
