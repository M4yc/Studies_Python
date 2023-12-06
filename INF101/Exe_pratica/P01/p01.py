# Nome do aluno:
# Matrícula:
# Data: 
# (breve comentário dizendo o que o programa faz)

from math import sqrt
import numpy as np
import imagens

def main():
    # Lê o arquivo com a imagem original e a coloca na matriz im.
    im = imagens.Imagem('fruits-700.jpg')
    im.mostrar()

    # Produz a imagem em tons de cinza em im1 a partir de im.
    print("Tons de cinza...")
    im1 = tonal(im)
    #im1.mostrar()
    
    # Produz as bordas da imagem em im2 a partir de im1.
    print("Detectando bordas...")
    im2 = sobel(im1)
    im2.mostrar()
    #im2.salvar('edge_image.png')
    
    print("Fim do processamento.")


# Implemente aqui a função tonal() que recebe uma imagem como parâmetro e
# retorna a imagem em tons de cinza.

...


# Implemente aqui a função sobel() que recebe uma imagem em tons de cinza e
# retorna a imagem contendo somente as bordas.

...

# Chama a função main para iniciar o processo.
main()
