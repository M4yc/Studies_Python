import  numpy as np

m = int(input("Numero de linhas: "))
n = int(input("Numero de colunas: "))

A = np.empty((m,n))
cont = 0
for i in range(0,m):
    for j in range(0,n):
        A[i][j] = float(input("Digite elementos A[%d][%d]: " % (i,j)))

x = float(input("Digite valor a ser verificado: "))

print('\nValores maiores que %d: '%x)
for i in range(0,m):
    for j in range(0,n):
        if A[i][j] > x:
            print(A[i,j], ',', end=' ')
