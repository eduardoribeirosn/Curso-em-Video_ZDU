pessoas = []
somaI = 0
while True:
    pessoa = {}
    nome = str(input('Nome: '))
    sexo = str(input('Sexo: [M/F] R: ')).strip().upper()[0]
    idade = int(input('Idade: '))
    somaI += idade
    pessoa = {
        'Nome': nome,
        'Sexo': sexo,
        'Idade': idade
    }
    pessoas.append(pessoa.copy())
    del pessoa
    while True:
        option = str(input('Quer continuar? (S/N) R: ')).strip().upper()[0]
        if option == 'S' or option == 'N':
            break
    if option == 'N':
        break
mediaI = somaI / len(pessoas)
print('-=' * 30)
print(f'- O grupo tem {len(pessoas)} pessoas.')
print(f'- A média de idade é de {mediaI} anos.')
print(f'- As mulheres cadastradas foram ', end='')
for c in range(0, len(pessoas)):
    if pessoas[c]['Sexo'] == 'F':
        print(f'[{pessoas[c]['Nome']}]', end=' ')
print()
print(f'- Lista das pessoas que estão acima da média:\n')
for c in range(0, len(pessoas)):
    if pessoas[c]['Idade'] > mediaI:
        print(f'{pessoas[c]}\n')
print('<< ENCERRADO >>')

