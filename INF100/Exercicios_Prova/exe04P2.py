import numpy as np

N = 6
A = np.array([5, 10, 36, 64, 255, 320])
#A = np.empty(N) #Para pedir ao usuario os numeros

totalvoto=0
soma = 0
#for i in range(N):   #Para pedir ao usuario os numeros
   # A[i] = int(input("Insira os votos do candidato %d: " % (i+1)))

for i in range(N):
    totalvoto+=A[i]

for i in range(N-1):
    soma +=A[i]

if soma < A[5]:
    print("Eleição definida em 1° Turno:")
    print("1° colocado: %d (%.2f%%)"%(A[5],(A[5] / totalvoto)*100))
    print("Soma dos demais: %d (%.2f%%)"%(soma,(100-(A[5] / totalvoto)*100)))
else:
    print("Haverá 2° Turno:")
    print("1° colocado: %d (%.2f%%)" % (A[5], (A[5] / totalvoto)*100))
    print("2° colocado: %d (%.2f%%)" % (A[4], (A[4] / totalvoto)*100))

