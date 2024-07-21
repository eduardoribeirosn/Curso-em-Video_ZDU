nomeC = input('Digite um Nome Completo: ').strip()
blocosNome = nomeC.split()
print('Primeiro: {}' .format(blocosNome[0]))
print('Último: {}' .format(blocosNome[len(blocosNome) - 1]))