#Escreva um programa que leia um vetor X de 10 elementos. Em seguida, crie um
#vetor Y da seguinte forma: os elementos de Y com índice par receberão os
#respectivos elementos de X divididos por 2; os elementos com índice ímpar
#receberão os respectivos elementos de X multiplicados por 3. Escrever o vetor X e o
#vetor Y.
import numpy as np
tamanho = 5
vetx = np.empty(tamanho)
for i in range (0,tamanho):
    vetx[i] = float(input("Informe o %d numero para o vetor: "%(i+1)))

vety = vetx[::-1]
#vety = list(reversed(vetx))
for i in range (0,tamanho):
    if vetx[i] % 2 == 0:
        vety[i] = vetx[i] / 2
    else:
        vety[i] = vetx[i] * 3

print("Vetor X:")
for i in range (0,tamanho):
    print("%.1f, " % vetx[i], end=' ')

print("\nVetor Y:")
for i in range(0, tamanho):
    print("%.1f, " % vety[i], end=' ')
