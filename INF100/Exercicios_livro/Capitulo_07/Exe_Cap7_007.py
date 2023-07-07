#Escreva um programa para ler um vetor SORTEADOS de 6 elementos contendo os
#números sorteados da Mega-Sena. A seguir, ler um vetor ESCOLHIDOS de até 15
#elementos contendo uma aposta. Uma aposta pode conter de 6 a 15 dezenas. Todos
#os valores devem estar entre 1 e 60. O programa deve garantir que as dezenas
#sorteadas sejam distintas, pois no mundo real se uma dezena sorteada for repetida,
#ela é descartada. O mesmo vale para as dezenas da aposta do usuário. O
#programa deve exibir as dezenas “sorteadas”, as dezenas da aposta e escrever
#quais números da aposta correspondem a números sorteados e quantos pontos ele
#fez.

import numpy as np
tamanho1 = 6
tamanho2 = 6
print("Programa da Mega-Sena.")
print('')
sorteados = np.empty(tamanho1)
escolhidos = np.empty(tamanho2)

#leitura para o vetor Sorteados
print('Digite os números sorteados da Mega-Sena:')

for i in range (0,tamanho1):
    valor = float(input("%d° numero de [1 a 60]: "%(i+1)))
    while valor in sorteados:
        print("Valor Invalido! Numero repetido.")
        valor = float(input("%d° numero de [1 a 60]: " % (i + 1)))
    while valor < 1 or valor > 60:
        print("Valor Invalido!")
        valor = float(input("%d° numero de [1 a 60]: " % (i + 1)))
    sorteados[i] = valor

#leitura para o vetor escolhidos
print('\nValores Escolhidos')
for i in range (0,tamanho2):
    valor = float(input("%d° numero de [1 a 60]: "%(i+1)))
    while valor in escolhidos:
        print("Valor Invalido! Numero repetido.")
        valor = float(input("%d° numero de [1 a 60]: " % (i + 1)))
    while valor < 1 or valor > 60:
        print("Valor Invalido!")
        valor = float(input("%d° numero de [1 a 60]: " % (i + 1)))
    escolhidos[i] = valor

print("\nNumeros Sorteados:")
for i in range (0,tamanho1):
    print("%.1f, " % sorteados[i], end=' ')

print("\nNumeros Escolhidos:")
for i in range(0, tamanho2):
    print("%.1f, " % escolhidos[i], end=' ')

pontos = 0
n=0
print("\n\nNumeros que você acertou:", end=' ')
for n in sorteados:
    if n in escolhidos:
        print("%d, " % n, end=' ')
        pontos +=1

print("\nVocê fez %d pontos na Mega-sena." % pontos)