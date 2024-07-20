carteira = float(input('Digite quanto você tem na carteira: '))
qdolar = carteira // 3.27
sobra = carteira % 3.27
print('Você pode comprar {} dolars, e sobrará R${:.2f}' .format(qdolar, sobra))52