#Faça um programa para ler um número entre 1 e 9 e mostrar a tabuada da
#multiplicação do número lido.
n = int(input("Infome um numero de 1 a 9 para ver a tabuada: "))
i = 1
while i <= 10:
    print("[%d] x [%d] = [%d]" %(i,n,(i*n)))
    i += 1