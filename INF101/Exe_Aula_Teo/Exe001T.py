import numpy as np

n = int(input("Informe o numero de alunos: "))

notas = np.zeros(n)

for i in range(0,n):
    notas[i] = float(input("Informe a %d° nota: " % (i+1)))
v = 0
maior =0
menor = notas[0]

for i in range(0,n):
    if notas[i] > maior:
        maior = notas[i]
    if notas[i] < menor:
        menor = notas[i]
    v += notas[i]

media = v / n
menorM = 0
for i in range(0,n):
    if notas[i] < media:
        menorM += 1

desvio_padrao = (Σ(xi - μ)^2 / N)^0.5

print("A media das notas fornecidas foi: %d" % media)
print("A maior nota foi: %d" % maior)
print("A menor nota foi: %d" % menor)
print("O numero de notas menor que a media foi: %d" % menorM)