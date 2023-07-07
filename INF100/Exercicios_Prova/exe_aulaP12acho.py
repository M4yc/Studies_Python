import imagens
nome = input('Informe o nome do arquivo: ')

im = imagens.Imagem(nome)
lin = im.altura

col = im.largura

print('O arquivo %s tem %d linhas e %d colunas.' %(nome,lin,col))
im.mostrar()

for i in range(0,lin):
    for j in range(0,col):
        if im[i,j]==(0,255,0):
            r, g, b = im[i-1][j]
            r1,g1,b1 = im[i+1][j]
            r2 = (r + r1)//2
            g2 = (g + g1) // 2
            b2 = (b + b1) // 2
            im[i][j] = (r2,g2,b2)
im.mostrar()
