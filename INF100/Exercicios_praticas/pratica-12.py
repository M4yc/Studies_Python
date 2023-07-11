# Nome do aluno:Maycon Vinicius
# Matrícula:113683
# Data:13/06/2023
# Programa que corrige uma imagem "corrompida" com pixels em verde

# importa a biblioteca de imagens
import imagens

# Solicita ao usuário o nome do arquivo
nome = input('Informe o nome do arquivo: ')
# Criar uma variável para guardar a imagem contida no arquivo cores_erro.png
im = imagens.Imagem(nome)
# descobre o número de linhas da imagem
lin = im.altura
# descobre o número de colunas da imagem
col = im.largura
# exibe no shell as informações sobre a dimensão da imagem
print('O arquivo %s tem %d linhas e %d colunas.' %(nome, lin, col))
# Exibe a imagem original (com erros de transmissão) na tela
im.mostrar()

######### complete o código abaixo desta linha ####################
for i in range(0,lin):
    for j in range(0,col):
        if im[i][j]==(0,255,0):
            r, g ,b = im[i-1][j]
            rb, gb, bb = im[i+1][j]
            rm = (r + rb)//2
            gm = (g + gb)//2
            bm = (b + bb)//2
            im[i][j]=(rm,gm,bm)
            
im.mostrar()
