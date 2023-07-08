import numpy as np

dimensao = 10
# Definir um arranjo bidimensional de inteiros com valores [1, 10]

matriz = np.random.randint(1, 11, (dimensao, dimensao))
somaLin = np.empty(dimensao, dtype=int)
for j in range( 0, dimensao ):
    somaLin[j] = 0
    for i in range( 0, dimensao ):
        somaLin[j] = somaLin[j] + matriz[j][i]

print(matriz)
print('---------------')
print(somaLin)