import imagens
def inicImagem() :
    #nome = input('Nome do arquivo: ')
    nome = 'cores.png'
    im = imagens.Imagem(nome)
    # descobre o número de linhas da imagem
    linha = im.altura
    # descobre o número de colunas da imagem
    coluna = im.largura

    return im, linha, coluna


inicImagem()
