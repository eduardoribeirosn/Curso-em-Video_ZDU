# c = (
#     '\033[m',       # 0 = sem cor
#     '\033[0;31m',   # 1 = vermelho
#     '\033[0;32m',   # 2 = verde
#     '\033[0;33m',   # 3 = amarelo
#     '\033[0;34m',   # 4 = azul
#     '\033[0;35m',   # 5 = roxo
#     '\033[1;37m'    # 6 = branco
#     )
# def menuP():
#     while True:
#         print(f'{c[6]}-' * 50)
#         print(f'{c[6]}{"MENU PRINCIPAL":^50}')
#         print(f'{c[6]}-' * 50)
#         print(f'{c[3]}1 {c[6]}- {c[4]}Ver pessoas cadastradas{c[0]}')
#         print(f'{c[3]}2 {c[6]}- {c[4]}Cadastrar nova Pessoa{c[0]}')
#         print(f'{c[3]}3 {c[6]}- {c[4]}Sair do Sistema{c[0]}')
#         print(f'{c[6]}-' * 50)
#         try:
#             opcao = int(input(f'{c[3]}Sua Opção: {c[2]}'))
#         except (ValueError, TypeError):
#             print(f'{c[1]}ERRO: por favor, digite um número inteiro válido.{c[0]}')
#             continue
#         else:
#             if opcao < 1 or opcao > 3:
#                 print(f'{c[1]}ERRO: Digite uma opção válida!{c[0]}')
#             if opcao == 3:
#                 print(f'{c[2]}Saindo do Sistema...{c[0]}')
#                 return 0





# PROF JEITO 

def leiaInt(text):
    while True:
        try:
            num = int(input(text))
        except (ValueError, TypeError):
            print(f'\033[1;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[1;33mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return num


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[33mSua Opção: \033[m')
    return opc


