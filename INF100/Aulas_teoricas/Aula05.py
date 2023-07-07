#Calculo da media abordagem (1)
n = int(input("Quantos valores vão ser fornecidos: "))
i =0
soma = 0

while i < n:
    valor = float(input("Entre com um valor: "))
    soma += valor
    i += 1
media = soma/n
print(f"\nMedia = {media}")