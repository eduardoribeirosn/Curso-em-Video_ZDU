city = input('Digite uma cidade: ')
grande = city.upper()
onde = grande.find('SANTO')
if(onde == 0):
    print('Sim')
else: 
    print('Não')