#Escreva um programa para ler um número inteiro e escrever se ele é par ou ímpar.
n = int(input("Insira um numero inteiro maior que zero: "))

if n % 2 == 0:
    print("O número %d é par." % n)
else:
    print(f"O número {n} é impar.")