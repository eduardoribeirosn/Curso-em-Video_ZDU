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

    print(f'{"N°":<4}{"NOME":<10}{"MÉDIA":>8}')


# OUUUUUUUUUUU

# ficha = []
# while True:
#     nome = str(input('Nome: '))
#     nota1 = float(input('Nota 1: '))
#     nota2 = float(input('Nota 2: '))
#     media = (nota1 + nota2) / 2
#     ficha.append([nome, [nota1, nota2], media])
#     resp = str(input('Quer continuar? [S/N] '))
#     if resp in 'Nn':
#         break
# print('-=' * 30)
# print(f'{"N°.":<4}{"NOME":<10}{"MÉDIA":>8}')
# print('-=' * 26)
# for i, a in enumerate(ficha):
#     print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
# while True:
#     print('-' * 35)
#     opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
#     if opc += 999:
#         print('FINALIZANDO...')
#         break
#     if opc <= len(ficha) - 1:
#         print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
# print('<<< VOLTE SEMPRE >>>')