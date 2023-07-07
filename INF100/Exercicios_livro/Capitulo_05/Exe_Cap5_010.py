# Escreva um programa que leia as medias (a, b e c) dos lados de um suposto
#triângulo e escreva se essas medidas podem formar um triângulo ou não. Caso
#firmativo, dizer seu tipo (equilátero ou isósceles ou escaleno). A condição de
#existência de um triângulo é dada por:
#- | b − c | < a < b + c
#- | a − c | < b < a + c
#- | a − b | < c < a + b
a = int(input("Digite a medida de a= "))
b = int(input("Digite a medida de b= "))
c = int(input("Digite a medida de c= "))

if a + b > c and b + c > a and a + c > b:
    if a == b == c:
        print("É um triângulo equilátero.")
    elif a == b or b == c or a == c:
        print("É um triângulo isósceles.")
    else:
        print("É um triângulo escaleno.")
else:
    print("Não tem como.")