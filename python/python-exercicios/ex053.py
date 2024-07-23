frase = input('Digite uma frase: ').lower().strip().split()
frase = "".join(frase)
frasei = frase[len(frase):: - 1] # ou frase[:: - 1]
print('O inverso de {} é {}' .format(frase.upper(), frasei.upper()))
if frase == frasei:
    print('A frase é um palíndromo!')
else:
    print('A frase Não é um palíndromo!')
# print(frase[0:len(frase):1])
# print(frase[len(frase):: - 1])
