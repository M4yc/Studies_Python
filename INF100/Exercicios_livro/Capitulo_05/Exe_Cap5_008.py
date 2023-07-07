#Escreva um programa que leia três valores e imprima o maior deles.
n1 = int(input("Insira um valor: "))
n2 = int(input("Insira outro valor: "))
n3 = int(input("Insira outro valor: "))

if n1 > n2 and n1 > n3:
    print("%d é o maior valor inserido."%n1)
elif n2 > n1 and n2 > n3:
    print("%d é o maior valor inserido."%n2)
elif n3 > n1 and n3 > n2:
    print("%d é o maior valor inserido."%n3)
