#Faça um programa que receba 2 números inteiros e imprima o maior deles, ou informe que os dois são iguais.
n = int(input("Insira um numero: "))
n2 = int(input("Insira outro numero: "))

if n > n2:
    print("O [%d] primeiro numero que você digitou é maior que o segundo [%d]." %(n,n2))
elif n2 > n:
    print("O [%d] Segundo numero que você digitou é maior que o primeiro [%d]."%(n2,n))
else:
    print("Os numeros são iguais.")