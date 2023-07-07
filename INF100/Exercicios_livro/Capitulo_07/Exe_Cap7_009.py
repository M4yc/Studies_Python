#Escreva um programa para ler um vetor A de 10 elementos e um valor X. Copie para
#um vetor S os elementos de A que são maiores que X. Logo após imprima o vetor S.
import numpy as np

tamanho = 5
A = np.empty(tamanho)
vets = np.empty(tamanho)
cont = 0

for i in range (0,tamanho):
    A[i] = float(input("Informe o %d numero para o vetor: "%(i+1)))
X = int(input("Informe o valor de X: "))
for i in range(0,tamanho):
    if A[i] > X:
        vets[i] = X

print('Valores maiores que %d: ' % X)
for i in range(0,tamanho):
    if A[i] > X:
        vets[i]=X
        print(vets[i],',',end=' ')