#Faça um programa que leia um vetor e ordene, de modo crescente, o vetor

import numpy as np
tamanho = 5
vetx = np.empty(tamanho)
for i in range (0,tamanho):
    vetx[i] = float(input("Informe o %d numero para o vetor: "%(i+1)))

vetx.sort()

print("Vetor em ordem crescente:")
for i in range (0,tamanho):
    print("%.1f, " % vetx[i], end=' ')