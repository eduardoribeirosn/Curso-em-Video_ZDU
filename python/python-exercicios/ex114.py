import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com')
except urllib.error.URLError:
    print('\033[0;31mErro na conexão com a internet ou a URL não foi encontrada!\033[m')
else:
    print('Conexão estabelecida com sucesso!')