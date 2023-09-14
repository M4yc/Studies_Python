import random
import numpy as np
def main():
    #l=[22,1,4,2,5,65,7,85,9]
    #l=[36]
    l=[14,54,24,75,11,77,23,11]
    #l=[]
    #l=[random.randint(0,100) for i in range(9)]
    print("Lista Original: ",l)

    print("Segundo Menor valor da lista: ",segundoMenor(l))
    print("Lista Ordenada: ",mini(l))
def mini(l):
    lista = l
    #lista.sort()
    #np.min(lista)

    return np.
def segundoMenor(l):
    lista = l
    menor = l[0]
    menor2 = l[0]
    if len(l) > 1:
        for i in range(len(l)):
            for j in range(len(l)):
                if l[i] < menor:
                    menor = l[i]
                if l[j] < menor2 and l[j] > menor:
                    menor2 = l[j]
                elif l[i] == menor:
                    menor2 = l[j]
        return menor2
    else:
        return None


main()