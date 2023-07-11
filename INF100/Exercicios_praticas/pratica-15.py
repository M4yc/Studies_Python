# Nome do aluno:Maycon Vinicius Batista Araujo
# Matrícula:113683
# Data:04/07/2023
# Um programa que faz o quadrante ficar preto e branco

# importa a biblioteca de imagens
import imagens
import auxiliar2 as aux
##############################################################################
# ESCREVA abaixo desta linha o código para implementar a função processaImagem
def processaImagem(im,lin,col,dx,dy,quadrante):
    if quadrante == 1:
        for i in range(dx,lin//2):
            for j in range(dy,col//2):
                r,g,b = im[i][j]
                m = (r+g+b)//3
                im[i][j]=(m,m,m)
                
    if quadrante == 2:
        for i in range(0,lin//2):
            for j in range(col//2,col-1):
                r,g,b = im[i][j]
                m = (r+g+b)//3
                im[i][j]=(m,m,m)

    if quadrante == 3:
        for i in range(lin//2,lin-1):
            for j in range(0,col//2):
                r,g,b = im[i][j]
                m = (r+g+b)//3
                im[i][j]=(m,m,m)
    if quadrante == 4:
        for i in range(lin//2,lin-1):
            for j in range(col//2,col-1):
                r,g,b = im[i][j]
                m = (r+g+b)//3
                im[i][j]=(m,m,m)
                 

def main():
    # im = arranjo bidimensional com os pixels da imagem
    # lin = número de linhas da imagem
    # col = número de colunas da imagem
    im, lin, col = aux.abreArquivoImagem()

    # exibe a imagem original
    im.mostrar()

    # leitura e validação de um dos 4 quadrantes
    quadrante = aux.leiaInt('Informe o quadrante a ser modificado: ', 1, 4)   

    # definição do delocamento do quadrante selecionado (ou imagem completa)
    dx, dy = aux.calculaDeslocamentos(quadrante, lin, col)      

    # chamada da função para fazer o processamento da imagem
    #
    processaImagem(im, lin, col, dx, dy, quadrante)
    #

    # exibe a imagem após processamento
    im.mostrar()

# programa principal - executa a função main()
main()
