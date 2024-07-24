p1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite o número da razão: '))
for c in range(1, 11, 1):
    print('{} + ({} - 1) * {} = {}' .format(p1, c, r, ((c -1) * 10) + p1))

print('\nOU\n')

for c in range(1, 11, 1):
    print('{} ->' .format(((c - 1) * r) + p1), end=' ')
print('FIM..')

print('\nOu\n')

cont = 1
while cont != 11:
    print('{} ->' .format(((cont - 1) * r) + p1), end=' ')
    cont += 1
print('FIM..')