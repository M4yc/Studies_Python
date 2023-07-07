import numpy as np

l = 3
c = 3

A = np.empty((l, c))

print('Informe valores para o vetror A:')
for i in range(0,l):
    for j in range(0,c):
        A[i,j] = int(input("Elemento [%d] [%d]: " % (i,j)))

X = int(input("Valor a ser comparado: "))

print("Valores maiores que %d" % X)

for i in range(0,l):
    for j in range(0,c):
        if A[i,j] > X:
            print("%d,"%A[i,j], end=' ')