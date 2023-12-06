# Nome do aluno: Maycon Vinicius
# Matrícula:113683
# Data: 17/08/2023
# Programa que transforma a imagem em tons de cinza e filro sobel

from math import sqrt
import numpy as np
import imagens

def main():
    # Lê o arquivo com a imagem original e a coloca na matriz im.
    im = imagens.Imagem('pinwheel.jpg')
    im.mostrar()

    # Produz a imagem em tons de cinza em im1 a partir de im.
    print("Tons de cinza...")
    im1 = tonal(im)
    #im1.mostrar()
    
    # Produz o embossing da imagem em im2 a partir de im1.
    print("Detectando bordas...")
    im2 = sobel(im1)
    im2.mostrar()
    #im2.salvar('edge_image.png')
    
    print("Fim do processamento.")


# Implemente aqui a função tonal() que recebe uma imagem como parâmetro e
# retorna a imagem em tons de cinza.

def tonal(im):
    
    im1 = im.copiar()
    for i in range(0, im1.altura):
        for j in range(0, im1.largura):
            r, g, b = im1[i][j]
            lum = int(0.299 * r + 0.587 * g + 0.114 * b)
            im1[i][j] = (lum,lum,lum)

    return(im1)

            

# Implemente aqui a função sobel() que recebe uma imagem em tons de cinza e
# retorna a imagem contendo somente as bordas.

def sobel(im):
    im2 = im.copiar()
    bordas_im = np.zeros((im.altura, im.largura))
    
    filtro_vertical = [[-1, -2, -1],
                       [ 0, 0, 0],
                       [ 1, 2, 1]]
    
    filtro_horizontal = [[-1, 0, 1],
                         [-2, 0, 2],
                         [-1, 0, 1]]


    for y in range(1,im.altura-1):
        for x in range(1,im.largura-1):
            #Aplica o filtro Vertical
            pix = 0
            for i in range(0,3):
                for j in range(0,3):
                    r, g, b = im[y-(1-i)][x-(1-j)]
                    pix = pix + r * filtro_vertical[i][j]
            pontuacao_vert = pix/4

            #Aplica o filtro Horizontal
            pix = 0
            for i in range(0,3):
                for j in range(0,3):
                    r, g, b = im[y-(1-j)][x-(1-i)]
                    pix = pix + r * filtro_horizontal[j][i]
            pontuacao_horiz = pix/4
            
            pontuacao_borda = sqrt(pontuacao_vert**2 + pontuacao_horiz**2)
            bordas_im[y][x] = pontuacao_borda
    bordas_im = bordas_im/bordas_im.max()
    for y in range(1, im.altura-1):
        for x in range(1, im.largura-1):
            tom_cinza = int(bordas_im[y][x] * 255)
            im2[y][x] = (tom_cinza, tom_cinza, tom_cinza)

    return(im2)

# Chama a função main para iniciar o processo.
main()
