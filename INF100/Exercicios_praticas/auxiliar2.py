import imagens

def abreArquivoImagem() :
    nome = input('Nome do arquivo: ')
    im = imagens.Imagem(nome)
    # descobre o número de linhas da imagem
    linha = im.altura
    # descobre o número de colunas da imagem
    coluna = im.largura
    return im, linha, coluna

def calculaDeslocamentos(q, linha, coluna) :
    if q == 0 or q == 1 or q == 2:
        desl_linha = 0
    else:
        desl_linha = linha//2
    if q == 0 or q == 1 or q == 3:
        desl_coluna = 0
    else:
        desl_coluna = coluna//2
    return desl_linha, desl_coluna


def leiaInt( msg, vmin, vmax, mostraErro=True ):
    v = int( input( msg ))
    while v < vmin or v > vmax:
        if mostraErro:
            print('Valor deve estar entre', vmin, 'e', vmax )
        v = int( input( msg ))
    return v
