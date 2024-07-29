palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for c in palavras:
    print(f'\nNa palavra {c.upper()} temos', end=' ')
    for cont in c:
        if cont in 'aeiou':
            print(f'{cont}', end=' ')
        # if cont in 'e':
        #     print(f'e', end=' ')
        # if cont in 'i':
        #     print(f'i', end=' ')
        # if cont in 'o':
        #     print(f'o', end=' ')
        # if cont in 'u':
        #     print(f'u', end=' ')