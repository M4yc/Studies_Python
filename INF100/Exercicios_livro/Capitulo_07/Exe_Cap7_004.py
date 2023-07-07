#Faça um programa que leia um vetor W de 10 elementos, depois receba um valor V.
#Em seguida, seu programa deve contar e escrever quantas vezes o valor V ocorre
#no vetor W e escrever também em que posições (índices) do vetor W o valor V
#aparece.

import numpy as np
tamanho = 10
vetw = np.empty(tamanho)
for i in range (0,tamanho):
    vetw[i] = float(input("Informe o %d numero para o vetor: "%(i+1)))
v = float(input("Informe o valor para V: "))
c = 0
for i in range(0,tamanho):
    if v == vetw[i]:
        c +=1

if c > 0:
    print('\nO valor %d apareceu %d° vezes.' % (v, c))
    print("Na posição:", end=' ')
    for i in range(0,tamanho):
        if v == vetw[i]:
            print("%d, " % i, end=' ')
else:
    print('\nO valor %d não apareceu no vetor.' % v)