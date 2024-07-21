print('\033[1;33m-=-' * 20)
print('\033[1;35mAnalizador de Triângulos')
print('\033[1;33m-=-\033[m' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\n\033[32mOs segmentos acima PODEM FORMAR um triângulo!')
    if r1 == r2 and r1 == r3:
        print('\033[33mE ele é um Triângulo Equilátero!\033[m')
    elif r1 == r2 and r1 != r3 or r1 == r3 and r1 != r3 or r2 == r3 and r2 != r1:
        print('\033[33mE ele é um Triângulo Isósceles!\033[m')
    elif r1 != r2 and r1 != r3:
        print('\033[33mE ele é um Triângulo Escaleno!\033[m')
else:
    print('\033[1;31mOs segmentos acima NÂO PODEM FORMAR um triângulo!\033[m')