def notas(* num, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    maior = menor = total = soma = 0
    for valor in num:
        if maior == 0:
            maior = menor = valor
        elif valor > maior:
            maior = valor
        elif valor < menor:
            menor = valor
        total += 1
        soma += valor
    media = soma / total
    if media < 6:
        situacao = 'RUIM'
    elif media < 7:
        situacao = 'RAZOÁVEL'
    else:
        situacao = 'BOA'
    pessoa = {
        'Total': total,
        'Maior': maior,
        'Menor': menor,
        'Média': media,
    }
    if sit:
        pessoa['Situação'] = situacao
    
    print('-' * 40)
    return pessoa

# print()
# print(notas(3.5, 2, 6.5, 2, 7, 4))
# print()
help(notas)
