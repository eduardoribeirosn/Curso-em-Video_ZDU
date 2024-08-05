# Tratamento de ERRO!
try: # parte do código, que pode haver erro
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError): # Caso o erro seja um dos dois tipo, mostrar a mensagem abaixo!
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError: # Caso o erro seja este, mostrará a mensagem abaixo!
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt: # Caso o erro seja este, mostrará a mensagem abaixo!
    print('O usuário preferiu não informar os dados!')
except Exception as erro: # (except) parte do código, que vai aparecer caso haja erro. (Exception as erro) para mostrar a classe do erro
    print(f'Problema encontrado foi {erro.__class__}')
else: # Para mostrar caso não haja erro!
    print(f'O resultado é {r:.1f}')
finally: # Para mostrar independente se tem erro ou não!
    print('Volte sempre! Muito obrigado!')
