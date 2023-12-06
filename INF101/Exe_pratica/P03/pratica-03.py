#Nome: Maycon Vinicius
#Matricula:113683
#Data: 31/08/2023
#programa para ordenar lista em ordem crescente
    
#import random

def minimo(l,p):
    j = p
    for i in range(p,len(l)):
        if l[i] < l[j]:
            j = i        
    return j

def ordena(l):
    for h in range(0,len(l)-1):
        j=minimo(l,h)
        l[j], l[h] = l[h], l[j]
        
def main():
    l=[]
    #l=[random.randint(0,100) for i in range(7)]
    l =[36,18,43,9,18,25,14]
    print("Lista Original")
    for i in l:
        print(i,end=' ')
    
    print('\n')

    ordena(l)
    #ordenacao(l)
    
    print('\n')
    
    print("Lista Ordenada")
    for i in l:
        print(i,end=' ')

main()
