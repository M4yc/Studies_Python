import numpy as np

n = int(input("Informe o numero de alunos: "))

notas = np.zeros(n)

for i in range(0,n):
    notas[i] = float(input("Informe a %d° nota: " % (i+1)))
v = 0
for i in range(0,n):
    v += notas[i]

media = v / n

print(media)