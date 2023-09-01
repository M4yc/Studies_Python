import numpy
import random

def inverte(L):
    n = len(L)
    for i in range(n//2):
        L[i], L[n -i -1] = L[n -i -1],  L[i]


L = []
L = [random.randint(0,100) for i in range(10)]

print("Lista Original: ")
for i in L:
    print(i,end=' ')

inverte(L)
print("\n")
print("Lista Original: ")
for i in L:
    print(i,end=' ')