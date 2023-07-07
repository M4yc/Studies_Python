#Escreva um programa para ler um valor e escrever se ele é positivo ou negativo ou zero
n = int(input("Insira um numero: "))

if n==0:
    print("O número %d é zero." % n)
elif n > 0:
    print("O número %d é Positivo." % n)
else:
    print("O número %d é negativo." % n)