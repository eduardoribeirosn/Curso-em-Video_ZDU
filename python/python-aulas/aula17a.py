# Para adicionar um novo item a uma LISTA

lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']
lanche.append('Cookie') # Adiciona no final!

# Caso queira escolher o lugar que vai ser adicionado

lanche.insert(0, 'Hot Dog')

# Caso queira removar! 

del lanche [3] # Remover o item do índice 3
lanche.pop(3) # Também remover o item do índice 3
lanche.pop() # Quando não tem parametro, remove o último item
lanche.remove('Hot Dog') # Remove o item que tiver seu nome colocado no parametro

# Exemplo de remoção caso o item exista

if 'Pizza' in lanche:
    lanche.remove('Pizza')

# Para deixar a LISTA em ordem númerica

valores = [8, 2, 5, 4, 9, 3, 0]
valores.sort() # Para deixar em ordem númerica crescente
valores.sort(reverse=True) # Para deixar em ordem númerica Decrescente

# Para saber a quantidade de elementos existentes na LISTA

len(valores)

# Para criar uma cópia de uma LISTA (para mudar uma sem mudar a outra)

a = [1, 2, 4, 5]
# b = a ( FORMA ERRADA)
b = a[:] # Forma certa de criar uma cópia
b[2] = 8
