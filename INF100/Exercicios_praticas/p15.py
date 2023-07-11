# Nome do aluno: Maycon Vinicius Batista Araujo
# Matrícula: 113683
# Data: 10/07/2023
# Programa que faz o quadrante ficar preto e branco

# importa a biblioteca de imagens
import imagens
import auxiliar2 as aux
##############################################################################
# ESCREVA abaixo desta linha o código para implementar a função processaImagem
def processaImagem(im,lin,col,dx,dy,quadrante):

    if quadrante == 1:
        inicl = 0
        fiml = lin//2
        inicc = 0
        fimc = col//2
    if quadrante == 2:
        inicl = 0
        fiml = lin//2
        inicc = col//2
        fimc = col
    if quadrante == 3:
        inicl = lin//2
        fiml = lin
        inicc = 0
        fimc = col//2
    if quadrante == 4:
        inicl = lin//2
        fiml = lin
        inicc = col//2
        fimc = col

    if quadrante == 1:
        for i in range(dx, lin//2):
            for j in range(dy, col//2):
                r, g, b = im[i][j]
                m = (r+g+b)//3
                im[i][j] = (m, m, m)
    if quadrante == 2:
        for i in range(dx,lin//2):
            for j in range(dy,col):
                r,g,b = im[i][j]
                m = (r+g+b)//3
                im[i][j]=(m,m,m)
    
    """for i in range(inicl,fiml):
        for j in range(inicc,fimc):
            r,g,b = im[i][j]
            m = r+g+b//3
            x = r
            r = b
            b = x
            im[i][j] = (r,g,b)"""

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
