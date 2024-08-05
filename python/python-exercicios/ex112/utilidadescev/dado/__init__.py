def leiaDinheiro(text):
    while True:
        p = str(input(text)).replace(',', '.').strip()
        if p.isalpha() or p == '':
            print(f'\033[1;31mERRO: "{p}" é um preço inválido!\033[m')
        else:
            preco = float(p)
            return preco


