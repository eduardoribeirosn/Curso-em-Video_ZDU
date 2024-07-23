n = int(input('Digite um número: '))
tot = 0
for c in range(1, n + 1, 1):
    if n % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} \033[m' .format(c), end=' ')
print('\n\033[mO número {} foi divísivel {} vezes!' .format(n, tot))
if tot == 2:
    print('É por isso ele é PRIMO!')
else:
    print('É por isso ele NÃO é PRIMO!')
