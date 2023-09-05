import random
random.seed(113683)

l=[]
l=[random.randint(0,100)for i in range(6)]

#l=[1,2,3,4,5]
#l.insert(2,8)

for i in range(len(l)):
    print(l[i],end=' ')



print("\n")
print(max(l))
