#Aula de Arranjos
import numpy as np
print("Este programa faz a leitura de notas e informa a média, desvio padrão.")
print("a maior nota, menor nota e o numero de notas abaixo da média.")
n = int(input('Informe o numero de alunos da turma: '))
nota = np.empty(n)
soma = 0
maior = -1
menor = 101
for i in range (0,n):
    while True:
        nota[i] = float(input('Nota %d: ' %(i+1)))
        if nota[i] >= 0 and nota[i] <= 100:
            break
        else:
            print("Nota Invalida.")
    soma += nota[i]
    if nota[i] > maior:
        maior = nota[i]
    elif nota[i] < menor:
        menor = nota[i]
media = soma/n
soma=0
cnam=0
for i in range(0,n):
    soma = soma + (nota[1] - media)**2
    if nota[i] < media:
        cnam = cnam + 1
dp = (soma/n)**0.5
print('A média das notas é: %.2f' % media)
print('O desvio padrão das notas é: %.2f' % dp)
print('A maior nota é: %.2f' % maior)
print('A menor nota é: %.2f' % menor)
print('O numero de notas menor que a média é: %.2f' % cnam)
