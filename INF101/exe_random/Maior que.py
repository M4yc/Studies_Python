import numpy
import random

L = []
L = [random.randint(0,10)for i in range(10)]
C = []

print("Lista Original: ")
for i in L:
    print(i,end=' ')
print("\n")

x = int(input("Informe o valor de X: "))

for i in L:
    if i > x:
        C.append(i)

print(f"valores Maiores que {x}: ")

for i in range(len(C)):
    print(C[i],end=' ')