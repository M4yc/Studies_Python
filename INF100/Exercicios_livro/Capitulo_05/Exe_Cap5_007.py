#Faça um programa que leia 3 números inteiros (a, b e c) e diga se eles são números
#Pitagóricos, ou seja, se são da forma a² + b² = c².
a = int(input("Insira um valor para a: "))
b = int(input("Insira um valor para b: "))
c = int(input("Insira um valor para c: "))

if a**2 + b**2 == c**2:
    print("São Pitagóricos.")
else:
    print("Não são Pitagóricos.")