#Faça um programa que leia um arranjo de tamanho 10 e escreva o valor do maior
#elemento desse arranjo e a respectiva posição que ele ocupa no vetor.

import numpy as np
tamanho = 5
vetw = np.empty(tamanho)
for i in range (0,tamanho):
    vetw[i] = float(input("Informe o %d numero para o vetor: "%(i+1)))
maior = 0
posi = 0
for i in range(0,tamanho):
    if vetw[i] > maior:
        maior=vetw[i]
        posi = i

print("\nO maior valor desse vetor foi %d e aparece no indice %d do vetor." % (maior, posi))