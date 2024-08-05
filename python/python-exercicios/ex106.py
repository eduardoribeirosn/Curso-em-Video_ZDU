# from time import sleep
# def pyHelp():
#     cor0 = '\033[m'         # Sem cor
#     cor10 = '\033[37;41m'   # Fundo vermelho, letra branca
#     cor20 = '\033[37;42m'   # Fundo verde, letra branca
#     cor2 = '\033[32m'       # Letra verde
#     cor50 = '\033[1;37;44m' # Negrito, fundo azul, letra branca
#     cor7 = '\033[1;47m'     # Negrito, fundo branco
#     sistema = 'SISTEMA DE AJUDA PyHELP'
#     tam = (len(sistema) + 6)
#     while True:
#         print(cor20)
#         print('~' * tam)
#         print(f'{sistema:^{tam}}')
#         print('~' * tam, cor0)
#         funcao = str(input(f'Função ou Biblioteca > {cor2}')).strip().lower()
#         print(cor0, end='')
#         if funcao == 'fim':
#             sleep(0.5)
#             tchau = 'ATÉ LOGO!'
#             print(cor10)
#             print(f'~' * (len(tchau) + 6))
#             print(f'{tchau:^{len(tchau) + 6}}')
#             print(f'~' * (len(tchau) + 6), cor0)
#             sleep(0.5)
#             break
#         else:
#             acessando = f"Acessando o manual do comando '{funcao}'"
#             print(cor50)
#             print('~' * (len(acessando) + 6))
#             print(f'{acessando:^{len(acessando) + 6}}')
#             print('~' * (len(acessando) + 6), cor7)
#             sleep(1.5)
#             help(funcao)
#             print(cor0)
#             sleep(1.5)


# pyHelp()


# OUUUUUUU Método prof

from time import sleep
c = (
    '\033[m',          # 0 = sem cor
    '\033[0;30;41m',   # 1 = vermelho
    '\033[0;30;42m',   # 2 = verde
    '\033[0;30;43m',   # 3 = amarelo
    '\033[0;30;44m',   # 4 = azul
    '\033[0;30;45m',   # 5 = roxo
    '\033[7;30m'       # 6 = branco
    )

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[6], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


# Programa Principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)
