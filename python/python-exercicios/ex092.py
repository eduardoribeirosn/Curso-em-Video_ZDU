from datetime import date
anoa = date.today().year
pessoa = {}
nome = str(input('Nome: '))
anon = int(input('Ano de Nascimento: '))
ctps = int(input('Carteira de trabalho: (0 não tem): '))
idade = anoa - anon
if ctps > 0:
    anoc = int(input('Ano de contratação: '))
    sal = float(input('Salário: R$'))
    apos = idade + ((anoc - anoa) + 35)
    pessoa = {
        'Nome': nome,
        'Idade': idade,
        'Ctps': ctps,
        'Anoc': anoc,
        'Salário': sal,
        'Aposentadoria': apos
    }
else: 
    pessoa = {
        'Nome': nome,
        'Idade': idade,
        'Ctps': ctps
    }
print('-=' * 30)
print(pessoa)
print(f'Nome tem o valor {pessoa['Nome']}')
print(f'Idade tem o valor {pessoa['Idade']}')
print(f'Ctps tem o valor {pessoa['Ctps']}')
if pessoa['Ctps'] > 0:
    print(f'Contratação tem o valor de {pessoa['Anoc']}')
    print(f'Salário tem o valor {pessoa['Salário']}')
    print(f'Aposentadoria tem o valor {pessoa['Aposentadoria']}')


