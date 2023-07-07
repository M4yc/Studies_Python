#Programa para calculo de area de um triangulo
#Área=  p(p-a)(p-b)(p-c)**(1/2)
#P= (a+b+c)/2
print('Entre com os valores dos lados de um triângulo:')
a = float(input(("a = ")))
b = float(input(("b = ")))
c = float(input(("c = ")))

p = (a+b+c)/2
area = (p*(p-a)*(p-b)*(p-c))**(1/2)

print('Área = ', area)