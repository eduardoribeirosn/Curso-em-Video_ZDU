aluno = []
while True:
    pessoa = [[[]]]
    pessoa.append(str(input('Nome: ')))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    pessoa[0].append(n1)
    pessoa[0].append(n2)
    pessoa[0][0].append((n1 + n2) / 2)
    aluno.append(pessoa[:])
    pessoa.clear()
    while True:
        option = str(input('Quer continuar? (S/N) R: ')).strip().upper()[0]
        if option == 'S' or option == 'N':
            break
    if option == 'N':
        break
print('-=' * 30)
print('N°  NOME', end='')
print(f'{'MÉDIA':^25}')
print('-' * 30)
for pos, p in enumerate(aluno):
    print(f'{pos}   {p[1]:<18}', end='')
    print(f'{p[0][0]}')
while True:
    print('-' * 50)
    na = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if na == 999:
        break
    print(f'Notas de {aluno[na][1]} são {aluno[na][0][1:3]}')
