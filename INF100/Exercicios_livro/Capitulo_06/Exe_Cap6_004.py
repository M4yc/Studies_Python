# Faça um programa que receba um inteiro N e calcule os seus divisores.
i = 1
n = int(input("Informe um numero inteiro: "))

while i <= n:
    if n % i == 0:
        print(i)
    i += 1

