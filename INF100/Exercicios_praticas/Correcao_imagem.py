import imagens


#nome = input('Nome do arquivo: ')
nome = 'cores.png'
im = imagens.Imagem(nome)
# descobre o número de linhas da imagem
lin = im.altura
# descobre o número de colunas da imagem
col = im.largura

for i in range(0,lin):
    for j in range(0,col):
        if im[i][j]==(0,255,0):
            r, g ,b = im[i-1][j]
            rb, gb, bb = im[i+1][j]
            rm = (r + rb)//2
            gm = (g + gb)//2
            bm = (b + bb)//2
            im[i][j]=(rm,gm,bm)