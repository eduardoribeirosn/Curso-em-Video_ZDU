pessoa = {}
pessoa['nome'] = str(input('Nome: '))
pessoa['média'] = float(input('Média: '))
if pessoa['média'] >= 6:
    situacao = 'Aprovado(a)!'
else:
    situacao = 'Reprovado(a)!'
pessoa['situação'] = situacao
print(f'Nome é igual a {pessoa['nome']}')
print(f'Média é igual a {pessoa['média']}')
print(f'Situação é igual a {pessoa['situação']}')
