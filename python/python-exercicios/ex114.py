import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com')
except urllib.error.URLError:
    print('\n\033[1;31mErro na conexão com a internet ou a URL não foi encontrada!\033[m\n')
else:
    print('\n\033[0;32mConexão estabelecida com sucesso!\033[m\n')
    # print(site.read())
