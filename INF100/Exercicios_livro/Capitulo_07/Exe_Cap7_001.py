#Modificação de vetor
import numpy as np
vet = np.empty(10)
for i in range (0,10):
    vet[i] = float(input("Informe o numero desejado: "))
    if vet[i] < 0:
        vet[i] = 0

print('')
for i in range (0,10):
    print(f"Valores digitados : {vet[i]}")
