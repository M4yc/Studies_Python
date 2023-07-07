#Escreva um programa que leia 4 números inteiros e calcule a soma dos que forem par.
n = int(input("Insira um numero: "))
n2 = int(input("Insira outro numero: "))
n3 = int(input("Insira outro numero: "))
n4 = int(input("Insira outro numero: "))
soma = 0

if n % 2 ==0:
    soma=n
if n2 % 2 == 0:
    soma += n2
if n3 % 2 == 0:
    soma += n3
if n4 % 2 ==0:
    soma += n4


print("Soma = %d"%soma)