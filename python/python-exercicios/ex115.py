from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'python/python-exercicios/ex115/cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('\033[32mSaindo do sistema... Até logo!\033[m')
        break
    else:
        cabecalho('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
