import  numpy as np

m = int(input("Numero de linhas: "))
n = int(input("Numero de colunas: "))

A = np.empty((m,n))
for i in range(0,m):
    for j in range(0,n):
        S = 'Digite elementos A[%d][%d]: ' % (i,j)
        A[i][j] = float(input(S))

diagonal = True

for i in range(0,m):
    for j in range(0,n):
        if i != j and A[i][j] != 0:
            diagonal = False

if diagonal:
    print("É uma matriz diagonal.")
else:
    print("Não é uma matriz diagonal.")