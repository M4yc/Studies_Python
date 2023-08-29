import random
def ordem(list):
    n = len(list)
    for i in range(n):
        min_index = i
        for j in range(i,n):
            if list[j] < list[min_index]:
                min_index = j
        list[i],list[min_index] = list[min_index], list[i]


list=[]
list =[random.randint(0,100) for i in range(10)]



print("Lista Original")
for i in list:
    print(i,end=' ')

print('\n')

#ordem(list)
list.sort()

print("Lista Ordenada")
for i in list:
    print(i,end=' ')


