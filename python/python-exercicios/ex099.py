# def maior(* num):
#     maior = 0
#     for c in range(0, len(num)):
#         if c == 0:
#             maior = num[0]
#         if num[c] > maior:
#             maior = num[c]
#     print('-=' * 30)
#     print(maior)



# maior(3, 5, 2, 9, 4, 7, 8)


# OUUUU minha forma tbm

from time import sleep
def maior(* num):
    maior = 0
    print('-=' * 30)
    print('Analizando os valores passados...')
    for valor in num:
        if maior == 0 or valor > maior:
            maior = valor
        print(valor, end=' ', flush=True)
        sleep(0.2)
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
print()