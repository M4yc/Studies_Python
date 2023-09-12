import random
random.seed(113683)

l=[]
l=[random.randint(0,100)for i in range(6)]

#l=[1,2,3,4,5]
#
l.insert(2,8)

for i in range(len(l)):
    print(l[i],end=' ')


print("\n")
print(f"Maximo: {max(l)}")
#print(max(l))
print(f"Pop: {l.pop()}")
#print(l.pop())
print(f"Lista depois do Pop:{l}")

