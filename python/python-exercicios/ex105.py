def notas(* num, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    if sum(num)/len(num) < 5:
        situacao = 'RUIM'
    elif sum(num)/len(num) < 7:
        situacao = 'RAZOÁVEL'
    else:
        situacao = 'BOA'
    pessoa = {
        'Total': len(num),
        'Maior': max(num),
        'Menor': min(num),
        'Média': sum(num)/len(num),
    }
    if sit:
        pessoa['Situação'] = situacao
    
    print('-' * 40)
    return pessoa


print()
print(notas(5.5, 2.5, 1.5, sit=True))
print()
# help(notas)
