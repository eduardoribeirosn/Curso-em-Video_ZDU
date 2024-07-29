valores = (int(input('Digite o primeiro valor: ')), int(input('Digite o segundo valor: ')), int(input('Digite o terceiro valor: ')), int(input('Digite o quarto valor: ')))
print(f'\nOs números Digitados foram: ', end='')
print(f'{valores[0]} {valores[1]} {valores[2]} {valores[3]}')
if valores.count(9) == 1:
    print(f'\nO número 9 aparece uma vez.')
else:
    print(f'\nO número 9 aparece {valores.count(9)} vezes.')
if valores.count(3) == 0: # ou if 3 in valores:
    print(f'O valor 3 não foi digitado em nenhuma posição.')
else:
    print(f'O valor 3 apareceu na {valores.index(3) + 1}° posição.')
print('Os valores pares digitados foram', end=' ')
for c in valores:
    if c % 2 == 0:
        print(c, end=' ')
print('.')
