import numpy as np

# jogo da velha
def inicializaTabuleiro(l, c):
    A = np.empty((l,c), dtype=str)
    # preencher o tabuleiro vazio for i in range (0, l) : # linhas
    for i in range (0, l) :
        for j in range (0, c) : # colunas
            A[i][j] = '-'
    return A

def imprimeTabuleiro(A):
    l, c = np.shape(A) # descobre o número de linhas e colunas do arranjo A
    for i in range (0, l) : # linhas
        # imprime 1 linha
        for j in range (0, c) : # colunas    
            print(A[i][j], end='   ')
        print()
    print()

def inicializaJogo() :
    m = 'X'
    jog = 1
    return m, jog


