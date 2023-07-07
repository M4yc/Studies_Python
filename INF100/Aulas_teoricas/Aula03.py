#Programa de equação de segundo grau ax²+bx+c=0
#Δ=b²-4*a*c
#X1=-b+√Δ/2*a
#X2=-b-√Δ/2*a
print('Resolva sua Equação do 2°Grau ax²+bx+c=0')
a = float(input("Insira o valor de a: "))

#if a == 0:
#    a = float(input("Insira outro valor diferente de zero para a: "))
while a == 0: #Maneira de receber somente valores diferentes de 0 para a
    a = float(input("Insira outro valor diferente de zero para a: "))

b = float(input("Insira o valor de b: "))
c = float(input("Insira o valor de c: "))

if a == 0:
    print('Essa não é uma equação do 2° Grau!')
else:
    d = b ** 2 - 4 * a * c
    if d == 0:
        print('Nenhuma raiz real.')
    else:
        x1 = (-b + d ** 0.5) / 2 * a
        x2 = (-b - d ** 0.5) / 2 * a
        print('O X1 vale: ', x1)
        print('O X2 vale: ', x2)
