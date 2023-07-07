#Escreva um programa que calcule o fatorial de N (N!), informado pelo usuário.
#Sendo que: N! = 1 * 2 * 3 * ... * (N - 1) * N. Por definição o fatorial de 0 é 1 (0! = 1).
#Caso o usuário digite um valor negativo, o programa deve informar que a função
#fatorial não está definida para números negativos e solicitar um novo número.
#N! = n* (n-1)*(n-2)....
print("Programa para calcular fatorial")

n = int(input("Infome um numero para calcular o fatorial:  "))

while n < 0:
    print("Função fatorial não está definida para números negativos.")
    n = int(input("Infome um numero para calcular o fatorial:  "))
if n == 0:
    print("Fatorial de (0! = 1)")
else:
    fatorial = 1
    i = 1
    while i <= n:
        fatorial *= i
        i += 1
    print("O fatorial de %d! é %d" %(n, fatorial))
