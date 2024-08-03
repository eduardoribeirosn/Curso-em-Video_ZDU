# Para transfomar uma varíavel local em global, utilize o comando (global)

def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
print()
print(f'A fora vale {a}\n')
teste(a)
print(f'\nA fora vale {a}')


# Retorno é bom para quando se quer colocar o resultado em uma varíavel!

def soma(a=0, b=0, c=0):
    s = a + b + c
    return s


n1 = soma(3, 5, 2)
n2 = soma(4, 1)
n3 = soma(6)
print(f'\nMeus resultados foram {n1}, {n2} e {n3}\n')