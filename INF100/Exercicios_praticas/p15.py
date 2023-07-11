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
    print("Opções para processamento da imagem.")
    print("[1] Para Trandormar em tons de cinza.")
    print("[2] Para Trocar o verde por vermelho.")
    print("[3] Para Trocar o azul por verde.")
    print("[4] Para trocar o vermelho por azul.")
    es = int(input("Sua escolha:"))
    while not es == 1 or es == 2 or es == 3 or es == 4:
        print("Opção não existente, escolha outra.")
        es = int(input("Sua escolha:"))
    if es == 1:#Preto e branco
        for i in range(0, lin//2):
            for j in range(0, col//2):
                r, g, b = im[dx+i][dy+j]
                m = (r+g+b)//3
                im[dx+i][dy+j] = (m, m, m)
    elif es == 2:#Verde por vermelho
        for i in range(0, lin//2):
            for j in range(0, col//2):
                r, g, b = im[i+dx][j+dy]
                g, r = r, g
                im[i+dx][j+dy] = (r, g, b)
    elif es == 3:#Vermelho por Azul
        for i in range(0, lin//2):
            for j in range(0, col//2):
                r, g, b = im[i+dx][j+dy]
                r, b = b, r
                im[i+dx][j+dy] = (r, g, b)
    elif es == 4:#Vermelho por Azul
        for i in range(0, lin//2):
            for j in range(0, col//2):
                r, g, b = im[i+dx][j+dy]
                r, b = b, r
                im[i+dx][j+dy] = (r, g, b)

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
