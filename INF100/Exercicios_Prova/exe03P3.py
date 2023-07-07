import numpy as np

#Class = np.zeros((4,4),dtype=int)

Class = np.array([[4, 4, 4, 0], [3, 5, 7, 0], [6, 6, 4, 0], [4, 4, 2, 0]])

for i in range(0,4):
    Class[i][3]=Class[i][1] - Class[i][2]

N = 4
maior = 0
nmaior = 0
for i in range(0,N):
    if Class[i][0] > maior:
        maior = Class[i][0]
        nmaior = 1
    elif maior == Class[i][0]:
        nmaior += 1

print(Class)
print('--------------------')
print(nmaior,'Seleções fizeram',maior,'pontos')