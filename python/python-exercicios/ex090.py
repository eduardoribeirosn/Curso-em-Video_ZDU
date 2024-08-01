pessoa = {}
pessoa['nome'] = str(input('Nome: '))
pessoa['média'] = float(input(f'Média de {pessoa["nome"]}: '))
if pessoa['média'] >= 7:
    situacao = 'Aprovado(a)!'
elif 5 <= pessoa['média'] < 7:
    situacao = 'Recuperação!'
else:
    situacao = 'Reprovado(a)!'
pessoa['situação'] = situacao
# print(f'Nome é igual a {pessoa['nome']}')
# print(f'Média é igual a {pessoa['média']}')
# print(f'Situação é igual a {pessoa['situação']}')

# Ou

print('-=' * 30)
for k, v in pessoa.items():
    print(f' - {k} é igual a {v}')
