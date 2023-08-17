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
media = sum(notas) / len(notas)

menorM = 0
for i in range(0,n):
    if notas[i] < media:
        menorM += 1

soma_quadrados_diferencas = sum((x - media) ** 2 for x in notas)
variancia = soma_quadrados_diferencas / len(notas)
desvio_padrao = variancia ** 0.5

print("Desvio Padrão:", desvio_padrao)
print("A media das notas fornecidas foi: %d" % media)
print("A maior nota foi: %d" % maior)
print("A menor nota foi: %d" % menor)
print("O numero de notas menor que a media foi: %d" % menorM)