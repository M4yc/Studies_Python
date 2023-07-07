#Faça um programa que leia 2 números inteiros. Se o segundo for diferente de zero,
#calcular e imprimir o quociente do primeiro pelo segundo. Caso contrário, imprimir a
#mensagem: “DIVISÃO POR ZERO”.

n = int(input("Insira um numero: "))
n2 = int(input("Insira outro numero: "))

if n2 !=0:
    div = n/n2
    print("A divisão de %d por %d é = %.2f "%(n,n2,div))
else:
    print("Divisão por zero.")
