# Dicionários

# Para criar um dicionário

# pessoa1 = dict() or pessoa1 = {}

pessoa1 = {
    'nome': 'Zduardo',
    'idade': 18
}

# Para adicionar!

pessoa1['sexo'] = 'M'

# Para deletar!

del pessoa1['idade']

# Mostrando o sentido de (value, keys, items)

filme = {
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}

print(filme.values()) # Para mostrar os valores ('Star Wars', 1977, 'George Lucas')
print(filme.keys()) # Para mostrar as chaves ('titulo', 'ano', 'diretor')
print(filme.items()) # Para mostrar os 2 de cima!!