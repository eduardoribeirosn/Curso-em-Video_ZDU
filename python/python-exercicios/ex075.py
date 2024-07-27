n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
n4 = int(input('Digite o quarto valor: '))
valores = (n1, n2, n3, n4)
print(f'\nOs números Digitados foram: ', end='')
print(f'{valores[0]} {valores[1]} {valores[2]} {valores[3]}')
if valores.count(9) == 1:
    print(f'\nO número 9 aparece uma vez.')
else:
    print(f'\nO número 9 aparece {valores.count(9)} vezes.')
# NÃO SEI COLOCAR EM QUAL POSIÇÃO O 3 FOI COLOCADO!
# print(f'O valor 3 apareceu na {valores.index(3) + 1}° posição')
# print(f'O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram', end=' ')
for c in valores:
    if c % 2 == 0:
        print(c, end=' ')
