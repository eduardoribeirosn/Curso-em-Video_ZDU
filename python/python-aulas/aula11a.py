# Cores no Terminal

# Padrão ANSI

# \033[0:33:44m

# \033[ = comando para cores

# 0 = Style da font (bons para uso ( 0: sem nada, 1: bold, 4: underline, 7: negativo(oq é fonte vai pra background, e oq é background vai pra fonte)))

# 33 = color do text (cores padrões do 30 ao 37 ( 30: cinza, 31: vermelho, 32: verde, 33: amarelo, 34: azul claro, 35: roxo parecido com azul [mais escuro], 36: ciano forte, 37: branco))

# 44 = background do texto (cores padrões do 40 ao 47 ( igual do text, porém começando com 4.. 40, 41, 42...))

# m = finalização do código

# TESTANDO...

# Tipo 1:
print('\033[4;33;40mTeste\033[m!')

# Tipo 2:
print('Olá {}Eduardo{}!' .format('\033[1;35m', '\033[m'))

# Tipo 3:
cores = {
    'Cor1': '\033[36m',
    'Cor2': '\033[33m',
    'Limpo': '\033[m'
}
print('{}Olá{}, {}Mundo{}!' .format(cores['Cor1'], cores['Limpo'], cores['Cor2'], cores['Limpo']))



# Desatualizado ( o que foi passado no vídeo)

# 33 = color do text (cores padrões do 30 ao 37 ( 30: branco, 31: vermelho, 32: verde, 33: amarelo, 34: azul, 35: roxo, 36: ciano, 37: cinza))