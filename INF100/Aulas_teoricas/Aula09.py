import imagens

im = imagens.Imagem('131.jpg')
im.mostrar()#Mostrar a imagem na tela

for i in range(0, im.altura):
    for j in range(0, im.largura):

        r, g, b =im[i][j]

        r = int(r* 0.9)
        g = int(g * 1.7)
        b = int(b * 0.9)

        im[i][j] = (r,g,b)
im.mostrar()