sexo = 'A'
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite um sexo: (M/F)\nR: ')).upper().strip()[0]
    if sexo != 'M' and sexo != 'F':
        print('Dados inválidos, Por favor, ', end=' ')
print('Concluido!')