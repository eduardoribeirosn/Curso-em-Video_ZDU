frase = input('Digite uma frase: ').strip()
print('A letra "A/a" apareceu {} vezes' .format(frase.lower().count('a')))
print('A primeira letra "A/a" apareceu na posição {}' .format(frase.lower().find('a') + 1))
print('A última letra "A/a" apareceu na posição {}' .format(frase.lower().rfind('a') + 1))