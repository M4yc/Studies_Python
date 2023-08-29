import random

import numpy

notas = []
notas = [random.randint(0,100) for _ in range(10)]
#for i in range(10):
    #notas[i] = random.randint(0,100)

soma = 0
for i in range(0,len(notas)):
    soma += notas[i]
print(f"Média: {soma/len(notas)}")
