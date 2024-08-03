from time import sleep
def pyHelp():
    cor0 = '\033[m'
    cor10 = '\033[37;41m'
    cor20 = '\033[37;42m'
    cor2 = '\033[32m'
    cor50 = '\033[1;37;44m'
    cor7 = '\033[1;47m'
    sistema = 'SISTEMA DE AJUDA PyHELP'
    tam = (len(sistema) + 6)
    while True:
        print(cor20)
        print('~' * tam)
        print(f'{sistema:^{tam}}')
        print('~' * tam, cor0)
        funcao = str(input(f'Função ou Biblioteca > {cor2}')).strip().lower()
        print(cor0, end='')
        if funcao == 'fim':
            sleep(0.5)
            tchau = 'ATÉ LOGO!'
            print(cor10)
            print(f'~' * (len(tchau) + 6))
            print(f'{tchau:^{len(tchau) + 6}}')
            print(f'~' * (len(tchau) + 6), cor0)
            sleep(0.5)
            break
        else:
            acessando = f"Acessando o manual do comando '{funcao}'"
            print(cor50)
            print('~' * (len(acessando) + 6))
            print(f'{acessando:^{len(acessando) + 6}}')
            print('~' * (len(acessando) + 6), cor7)
            sleep(1.5)
            help(funcao)
            print(cor0)
            sleep(1.5)


pyHelp()