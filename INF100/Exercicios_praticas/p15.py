# Nome do aluno:
# Matrícula:
# Data:
# Substitua esta linha pelo comentário dizendo o que o programa faz

# importa a biblioteca de imagens
import imagens
import auxiliar2 as aux
##############################################################################
# ESCREVA abaixo desta linha o código para implementar a função processaImagem





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
