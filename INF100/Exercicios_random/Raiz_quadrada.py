#while True:
   # x = int(input("Entre com um valor: "))
   # if x <= 0:
       # break

x = float(input("X= "))
erro = float(input("Erro= "))

r = x /2

while abs(r**2 - x) >= erro:
    r = (r + x/r) / 2

print("r= %f" % r)
print("r**2 = %2f" % r**2)