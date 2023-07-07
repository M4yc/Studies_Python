import  numpy as np

m = int(input("Numero de linhas: "))
n = int(input("Numero de colunas: "))

A = np.empty((m,n))
cont = 0
for i in range(0,m):
    for j in range(0,n):
        S = 'Digite elementos A[%d][%d]: ' % (i,j)
        A[i][j] = float(input(S))

x = float(input("Digite valor a ser verificado: "))
achou = False
for i in range(0,m):
    for j in range(0,n):
        if A[i][j] == x:
            achou = True

if achou:
    print(x,"apareceu na matriz")
else:
    print(x, "não apareceu na matriz")