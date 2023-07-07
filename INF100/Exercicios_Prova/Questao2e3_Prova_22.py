print("Entre com dois valores quaisquer.")
a = float(input("a = "))
b = float(input("b = "))
if a>b:
    aux = a
    a = b
    b = aux
print('Valores em ordem crescente %.2f e %.2f' %(a,b))
c = float(input("c = "))
if c<b:
    aux1 = b
    b=c
    c=aux1
elif c<a:
    aux2=a
    a=c
    c=aux2
print('Valores em ordem crescente %.2f, %.2f e %.2f' %(a,b,c))