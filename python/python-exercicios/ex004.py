algo = input('Digite algo: ')
print('Seu tipo é ({}).' .format(type(algo)))
print('É um número? ({}).' .format(algo.isnumeric()))
print('É decimal? ({}).' .format(algo.isdecimal()))
print('É alfanúmerico? ({}).' .format(algo.isalnum()))
print('É alfabético? ({}).' .format(algo.isalpha()))
print('Está tudo em maiusculo? ({}).' .format(algo.isupper()))
print('Está tudo em minusculo? ({}).' .format(algo.islower()))
print('Está capitalizada? ({})' .format(algo.istitle()))
print('É apenas espaços? ({})' .format(algo.isspace()))
