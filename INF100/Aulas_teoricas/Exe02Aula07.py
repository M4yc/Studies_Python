import  numpy as np

m = int(input("Numero de linhas: "))
n = int(input("Numero de colunas: "))

A = np.empty((m,n))

for i in range(0,m):
    for j in range(0,n):
        S = 'Digite elementos A[%d][%d]: ' % (i,j)
        A[i][j] = float(input(S))

x = float(input("Digite valor a ser verificado: "))
for i in range(0,m):
    for j in range(0,n):
        if A[i][j] == x:
            print(x,"aparece na posição(", i, ",", j, ")")
