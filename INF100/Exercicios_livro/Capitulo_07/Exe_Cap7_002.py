#Escreva um programa que leia um vetor X de 10 elementos. Crie um vetor Y, com
#todos os elementos de X na ordem inversa, ou seja, o último elemento passará a ser
#o primeiro, o penúltimo será o segundo e assim por diante. Escrever todo o vetor X e
#todo o vetor Y.
import numpy as np
tamanho = 5
vetx = np.empty(tamanho)
for i in range (0,tamanho):
    vetx[i] = float(input("Informe o %d numero para o vetor: "%(i+1)))

#vety = vetx[::-1]
vety = list(reversed(vetx))

print("Vetor X:")
for i in range (0,tamanho):
    print("%.1f, " % vetx[i], end=' ')

print("\nVetor Y:")
for i in range(0, tamanho):
    print("%.1f, " % vety[i], end=' ')
