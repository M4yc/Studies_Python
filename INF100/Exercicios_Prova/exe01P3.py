def funcao1(x,y):
    if x > y:
        return x+2
    else:
        return y-1

def funcao2(a,b,c):
    x = funcao1(a,b)
    y = funcao1(x,c)
    print(x,y)
    return y
#programa principal
r=0
x=5
y=3
z=9
print(r,x,y,z)
r = funcao1(r,z)
print(r,x,y,z)
z = funcao2(x,y,z)
print(r,x,y,z)
print(funcao1(x,y))
