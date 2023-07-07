#Calculo da media abordagem (2)
print("Programa de media das nota!")
n = soma = 0

while True:
    valor = float(input("Entre com um valor (< 0 para encerrar): "))
    if valor < 0:
        break
    soma += valor
    n+= 1

media = soma/n
print("\nMedia = %.2f" % media)