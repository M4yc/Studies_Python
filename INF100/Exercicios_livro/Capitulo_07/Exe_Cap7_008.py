#Refaça o programa anterior usando a função random.randint para sortear as 6
#dezenas, que deverão ser exibidas somente depois do usuário fazer a sua aposta.
#Nesta versão, o programa deverá informar o valor da aposta feita pelo usuário
#considerando que a aposta simples (6 dezenas) é de R$ 4,50 (valor em agosto de
#2020) e que os valores de outras apostas é dada pelo número de combinações
#possíveis, dada pela expressão:
# NúmeroDeCombinações =𝑛!/6!(𝑛−6)!, onde n = número de dezenas do palpite.
import random

import numpy as np
tamanho1 = 6

print("Programa da Mega-Sena.")
print('')
sorteados = np.empty(tamanho1)

#leitura para o vetor Sorteados
#print('Digite os números sorteados da Mega-Sena:')
for i in range (0,tamanho1):
    valor = random.randint(1,60)
    while valor in sorteados:
        valor = random.randint(1,60)
    while valor < 1 or valor > 60:
        valor = random.randint(1,60)
    sorteados[i] = valor

tamanho2 = int(input("Quantas apostas você vai fazer? "))
escolhidos = np.empty(tamanho2)

fatorial = 1
fatorial1 = 1
fatorialb = 1
i = 1
while i <= tamanho2:
    fatorial *= i
    i += 1
while i <= (tamanho2-6):
    fatorial1 *= i
    i += 1

ndc =fatorial/(720*fatorial1)
#Cada aposta é R$ 0,75
preco = 4.50

if tamanho2 == 6:
    preco = 4.50
else:
    preco += 0.75 * ndc

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
    print("%.2d, " % sorteados[i], end=' ')

print("\nNumeros Escolhidos:")
for i in range(0, tamanho2):
    print("%.2d, " % escolhidos[i], end=' ')

pontos = 0
n=0
print("\n\nNumeros que você acertou:", end=' ')
for n in sorteados:
    if n in escolhidos:
        print("%d, " % n, end=' ')
        pontos +=1

print("\nVocê fez %d pontos na Mega-sena." % pontos)
print("Valor da %d sua aposta na Mega-sena: %.2f" % (ndc,preco))