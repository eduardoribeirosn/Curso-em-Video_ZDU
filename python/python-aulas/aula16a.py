# Tuplas = () --- Lista = [] --- Dicionario = {}

# TUPLAS SÃO IMUTÁVEIS

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1]) # = Suco

print(lanche[-1]) # = Pudim

print(lanche[1:3]) # = Suco, Pizza

print(lanche[2:]) # = Pizza, Pudim

print(lanche[:2]) # = Hamburguer, Suco

print(lanche[-2:]) # = Pizza, Pudim

for comida in lanche:
    print(f'Eu vou comer {comida}!')

# ou 

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')

# ou

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi pacaz!!')

print(sorted(lanche)) # Aparace os lanches em ordem Alfabética... e por baixo dos panos transformou em LISTA []

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b # Não soma os valores, e sim junta as 2 varíaveis
print(c) # (2, 5, 4, 5, 8, 1, 2)
# Diferente de
c = b + a # Troca a ordem dos valores! primeiro os do B depois os do A

print(len(c)) # Mostra a quantidades de itens na Tupla

print(c.count(5)) # Mostra quantas vezes o 5 aparece na varíavel

print(c.index(8)) # Mostra o indice do número na varíavel

# Caso haja o número mais de 1 vez,
print(c)
print(c.index(5, 1)) # Irá procurar o 5, a partir do índice 1

# NO PYTHON, Tupla pode haver + de 1 tipo, como strings, int, float, na mesma Tupla

pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa) # Deleta a Tupla, (Pode apenas deletar a Tupla inteira)
print(pessoa)