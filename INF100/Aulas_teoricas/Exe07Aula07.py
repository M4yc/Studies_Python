import  numpy as np

m = int(input("Numero de linhas: "))
n = int(input("Numero de colunas: "))

A = np.empty((m,n))
for i in range(0,m):
    for j in range(0,n):
        S = 'Digite elementos A[%d][%d]: ' % (i,j)
        A[i][j] = float(input(S))

print("\nMatriz lida:\n")
for i in range(m):
    for j in range(n):
        print("%6.1f"%(A[i][j]), end='')
    print()

B = np.zeros(m)

for i in range(m):
    for j in range(n):
        B[i] += A[i][j]

C = np.zeros(n)
for i in range(m):
    for j in range(n):
        C[j] += A[i][j]

print('\nB =', end='')
for i in range(0,m):
    print("%6.1f" % (B[i]), end='')
print()

print('\nC =', end='')
for i in range(0,n):
    print("%6.1f" % (C[i]), end='')
print()
