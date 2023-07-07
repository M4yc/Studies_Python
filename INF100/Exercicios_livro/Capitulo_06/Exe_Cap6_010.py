#Faça um programa que receba dois números, inteiros e positivos a e b, e calcule 𝑎^𝑏
#sem usar a função ou o operador **.
a = int(input("Insira o valor de A: "))
b = int(input("Insira o valor de B: "))
i = 1
cal = 1
while i <= b:
    cal *= a
    i += 1

print("A elevado a B:", cal)
