# Nome do aluno:
# Matrícula:
# Data:
# Substitua esta linha pelo comentário dizendo o que o programa faz

# importa a biblioteca de imagens
import imagens
import auxiliar2 as aux

def processaImagem(imagem, lin, col, ic, jc) :

    for i in range(0, lin//2) :  
        for j in range (0, col//2):   
            r, g, b = imagem[ic+i][jc+j]
            # modifica o pixel i, j
            # descomente a linha do seu roteiro
            #1 - trocar tons vermelho e azul
            # turmas de 3a. feira 8h
            #r, b = b, r

            #2 - trocar tons vermelho e verde
            # turmas de 3a. feira 10h
            #r, g = g, r

            #3 tons de cinza
            # turmas de 3a. feira 14h
            #r = b = g = (r+g+b)//3
            
            
            # 4 azul = média de vermelho e verde
            # turmas de 3a. feira 16h
            #b = (r + g)//2

            # 5 negativo
            # turmas de 4a. feira 10h
            #r = 255-r
            #g = 255-g
            #b = 255-b
                                    
            # 6 - trocar tons verde e azul
            # turmas de 4a. feira 14h
            #g, b = b, g
            
                                    
            # 7 - vermelho = média de azul e verde
            # turmas de 4a. feira 16h
            #r = (b + g)//2
            
            # 8 - verde = média de vermelho e azul
            # turmas de 5a. feira 18h30
            #g = (r + b)//2

            imagem[ic+i][jc+j] = (r, g, b)

def main():
    # im = arranjo bidimensional com os pixels da imagem
    # lin = número de linhas da imagem
    # col = número de colunas da imagem
    im, lin, col = aux.abreArquivoImagem()
    # exibe a imagem original
    im.mostrar()
    # leitura e validação de um dos 4 quadrantes
    quadrante = aux.leiaInt('Informe o quadrante a ser modificado (1-4): ', 0, 4)   
    # definição do delocamento do quadrante selecionado
    dx, dy = aux.calculaDeslocamentos(quadrante, lin, col)      


    # processamento da imagem
    processaImagem(im, lin, col, dx, dy)


    # exibe a imagem após processamento
    im.mostrar()



# programa principal
#   observe a indentação do comando do  
#   programa principal na PRIMEIRA coluna
main()
