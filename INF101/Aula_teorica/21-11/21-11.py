#Aula de Try-execpt
def abrirArq(caminho):
    print()
try:
    caminho = "funcionarios.csv"
    #arquivo = open(caminho, 'r')

    with open(caminho, 'r') as arquivo:
        linhas = [l.rstrip() for l in arquivo.readline()]
        dados = []
        for l in linhas:
            d = tuple(l.split(','))
            dados.append(d)

    print(dados)
    #arquivo.close()
except FileExistsError:
    print('Arquivo não encontrado.')
except FileNotFoundError:
    print()